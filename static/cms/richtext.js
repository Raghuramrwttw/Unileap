// Turns every .ul-richtext block into a Quill WYSIWYG editor synced to its hidden textarea.
(function () {
  const toolbar = [
    [{ header: [2, 3, 4, false] }],
    ["bold", "italic", "underline", "strike"],
    [{ list: "ordered" }, { list: "bullet" }],
    ["blockquote", "link", "image"],
    [{ align: [] }],
    ["clean"],
  ];

  function init(root) {
    if (root.dataset.ready || !window.Quill) return;
    root.dataset.ready = "1";
    const textarea = root.querySelector("textarea");
    const editorEl = root.querySelector(".ul-richtext-editor");
    const quill = new Quill(editorEl, { theme: "snow", modules: { toolbar } });
    if (textarea.value) quill.clipboard.dangerouslyPasteHTML(textarea.value);
    quill.on("text-change", () => {
      textarea.value = quill.getText().trim().length || quill.root.querySelector("img") ? quill.root.innerHTML : "";
    });
  }

  function initAll() {
    // Skip the hidden "empty form" template rows of inlines.
    document.querySelectorAll(".ul-richtext").forEach((el) => {
      if (!el.closest(".empty-form")) init(el);
    });
  }

  document.addEventListener("DOMContentLoaded", initAll);
  document.addEventListener("formset:added", initAll);
})();
