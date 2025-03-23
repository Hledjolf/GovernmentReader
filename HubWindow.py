import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class DocumentReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Reader")

        # Create a menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # Add a file menu with a load document option
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Load Document", command=self.load_document)

        # Configure grid layout
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # Document text frame on the left
        self.document_frame = tk.Frame(self.root, bd=2, relief="sunken")
        self.document_frame.grid(row=1, column=0, rowspan=2, sticky="nsew", padx=5, pady=5)
        self.document_text = tk.Text(self.document_frame, wrap="word")
        self.document_text.pack(expand=True, fill="both")

        # Tags list frame on the upper right
        self.tags_frame = tk.Frame(self.root, bd=2, relief="sunken")
        self.tags_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.tags_label = tk.Label(self.tags_frame, text="Tags", font=("Arial", 14))
        self.tags_label.pack(anchor="w", padx=5, pady=5)
        self.filter_entry = tk.Entry(self.tags_frame)
        self.filter_entry.pack(fill="x", padx=5, pady=5)
        self.tags_listbox = tk.Listbox(self.tags_frame)
        self.tags_listbox.pack(expand=True, fill="both", padx=5, pady=5)

        # Comments text frame on the lower right
        self.comments_frame = tk.Frame(self.root, bd=2, relief="sunken")
        self.comments_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.comments_label = tk.Label(self.comments_frame, text="Comments", font=("Arial", 14))
        self.comments_label.pack(anchor="w", padx=5, pady=5)
        self.comments_text = tk.Text(self.comments_frame, wrap="word")
        self.comments_text.pack(expand=True, fill="both")

        # Sample data
        self.load_sample_data()

    def load_sample_data(self):
        sample_document_text = "This is a sample document text."
        self.document_text.insert("1.0", sample_document_text)

        sample_tags = ["Tag1", "Tag2", "Tag3"]
        for tag in sample_tags:
            self.tags_listbox.insert(tk.END, tag)

        sample_comments = "This is a sample comment text for the selected tag."
        self.comments_text.insert("1.0", sample_comments)

    def load_document(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                document_text = file.read()
                self.document_text.delete("1.0", tk.END)
                self.document_text.insert("1.0", document_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentReaderApp(root)
    root.mainloop()