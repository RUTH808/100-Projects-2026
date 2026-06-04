import customtkinter as ctk
from tkinter import filedialog, messagebox

from ui.toolbar import Toolbar
from ui.image_viewer import ImageViewer
from ui.parameter_panel import ParameterPanel
from ui.statistics_panel import StatisticsPanel
from ui.history_panel import HistoryPanel
from ui.pipeline_panel import PipelinePanel

from core.image_manager import ImageManager
from core.history_manager import HistoryManager
from core.operation_logger import OperationLogger
from core.statistics import ImageStatistics
from core.plugin_loader import PluginLoader
from core.pipeline_manager import PipelineManager
from core.batch_processor import BatchProcessor


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("OpenCV Image Studio")
        self.geometry("1800x950")
        self.minsize(1400, 800)

        self.image_manager = ImageManager()
        self.history = HistoryManager()
        self.logger = OperationLogger()
        self.pipeline_manager = PipelineManager()

        self.plugin_loader = PluginLoader()
        self.plugin_dict = self.plugin_loader.load_plugins()

        self.create_ui()

    def create_ui(self):

        Toolbar(self)

        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(fill="both", expand=True, padx=10, pady=10)

        # LEFT
        self.left_panel = ctk.CTkScrollableFrame(self.main_container, width=320)
        self.left_panel.pack(side="left", fill="y", padx=10)

        ctk.CTkButton(self.left_panel, text="Load Image",
                      command=self.load_image).pack(fill="x", padx=10, pady=3)

        ctk.CTkButton(self.left_panel, text="Save Image",
                      command=self.save_image).pack(fill="x", padx=10, pady=3)

        ctk.CTkButton(self.left_panel, text="Undo",
                      command=self.undo).pack(fill="x", padx=10, pady=3)

        ctk.CTkButton(self.left_panel, text="Redo",
                      command=self.redo).pack(fill="x", padx=10, pady=3)

        ctk.CTkLabel(self.left_panel, text="Plugins",
                     font=("Arial", 16, "bold")).pack(pady=(20, 5))

        self.plugin_menu = ctk.CTkComboBox(
            self.left_panel,
            values=list(self.plugin_dict.keys()),
            command=self.plugin_changed
        )
        self.plugin_menu.pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(self.left_panel, text="Apply Plugin",
                      command=self.apply_plugin).pack(fill="x", padx=10, pady=5)

        self.parameter_panel = ParameterPanel(self.left_panel)
        self.parameter_panel.pack(fill="x", padx=10, pady=10)

        self.pipeline_panel = PipelinePanel(self.left_panel)
        self.pipeline_panel.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(self.left_panel, text="Add To Pipeline",
                      command=self.add_to_pipeline).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Remove Selected",
                      command=self.remove_selected_step).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Move Up",
                      command=self.move_selected_up).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Move Down",
                      command=self.move_selected_down).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Run Pipeline",
                      command=self.run_pipeline).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Save Pipeline",
                      command=self.save_pipeline).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Load Pipeline",
                      command=self.load_pipeline).pack(fill="x", padx=10, pady=2)

        ctk.CTkButton(self.left_panel, text="Clear Pipeline",
                      command=self.clear_pipeline).pack(fill="x", padx=10, pady=2)

        ctk.CTkLabel(self.left_panel, text="Batch Processing",
                     font=("Arial", 16, "bold")).pack(pady=(20, 5))

        ctk.CTkButton(self.left_panel, text="Run Pipeline On Folder",
                      command=self.run_batch_pipeline).pack(fill="x", padx=10, pady=5)

        # CENTER
        self.center_panel = ctk.CTkFrame(self.main_container)
        self.center_panel.pack(side="left", fill="both", expand=True, padx=10)

        ctk.CTkLabel(self.center_panel, text="Original Image",
                     font=("Arial", 18, "bold")).grid(row=0, column=0, pady=10)

        ctk.CTkLabel(self.center_panel, text="Processed Image",
                     font=("Arial", 18, "bold")).grid(row=0, column=1, pady=10)

        self.original_label = ctk.CTkLabel(self.center_panel, text="")
        self.original_label.grid(row=1, column=0, padx=15, pady=15)

        self.processed_label = ctk.CTkLabel(self.center_panel, text="")
        self.processed_label.grid(row=1, column=1, padx=15, pady=15)

        self.zoom_frame = ctk.CTkFrame(self.center_panel)
        self.zoom_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ctk.CTkButton(self.zoom_frame, text="Zoom +",
                      command=self.zoom_in).pack(side="left", padx=5)
        ctk.CTkButton(self.zoom_frame, text="Zoom -",
                      command=self.zoom_out).pack(side="left", padx=5)
        ctk.CTkButton(self.zoom_frame, text="Fit",
                      command=self.fit_image).pack(side="left", padx=5)

        self.zoom_label = ctk.CTkLabel(self.zoom_frame, text="100%")
        self.zoom_label.pack(side="left", padx=10)

        # RIGHT
        self.right_panel = ctk.CTkFrame(self.main_container, width=350)
        self.right_panel.pack(side="right", fill="y", padx=10)

        self.statistics_panel = StatisticsPanel(self.right_panel)
        self.statistics_panel.pack(fill="x", pady=10)

        self.history_panel = HistoryPanel(self.right_panel)
        self.history_panel.pack(fill="both", expand=True, pady=10)

        if self.plugin_dict:
            first_plugin = list(self.plugin_dict.keys())[0]
            self.plugin_menu.set(first_plugin)
            self.plugin_changed(first_plugin)

    def plugin_changed(self, plugin_name):
        plugin = self.plugin_dict[plugin_name]
        params = getattr(plugin, "PLUGIN_PARAMS", {})
        self.parameter_panel.build(params)

    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")]
        )
        if not path:
            return
        self.image_manager.load(path)
        self.logger.add(f"Loaded image: {path}")
        self.history_panel.refresh(self.logger.get_logs())
        self.update_views()

    def update_views(self):
        if self.image_manager.original is None:
            return

        original = ImageViewer.convert(self.image_manager.original)
        current = ImageViewer.convert(self.image_manager.current)

        self.original_label.configure(image=original, text="")
        self.original_label.image = original

        self.processed_label.configure(image=current, text="")
        self.processed_label.image = current

        stats = ImageStatistics.get_stats(self.image_manager.current)
        self.statistics_panel.update_stats(stats)

    def apply_plugin(self):
        if self.image_manager.current is None:
            return

        plugin_name = self.plugin_menu.get()
        plugin = self.plugin_dict[plugin_name]
        params = self.parameter_panel.get_values()

        self.history.push(self.image_manager.current)
        self.image_manager.current = plugin.process(
            self.image_manager.current, params
        )

        self.logger.add(f"Applied {plugin_name}")
        self.history_panel.refresh(self.logger.get_logs())
        self.update_views()

    def undo(self):
        self.image_manager.current = self.history.undo(
            self.image_manager.current
        )
        self.update_views()

    def redo(self):
        self.image_manager.current = self.history.redo(
            self.image_manager.current
        )
        self.update_views()

    def zoom_in(self):
        ImageViewer.zoom_in()
        self.zoom_label.configure(text=f"{int(ImageViewer.zoom_factor*100)}%")
        self.update_views()

    def zoom_out(self):
        ImageViewer.zoom_out()
        self.zoom_label.configure(text=f"{int(ImageViewer.zoom_factor*100)}%")
        self.update_views()

    def fit_image(self):
        ImageViewer.fit()
        self.zoom_label.configure(text="100%")
        self.update_views()

    def add_to_pipeline(self):
        self.pipeline_manager.add_step(
            self.plugin_menu.get(),
            self.parameter_panel.get_values()
        )
        self.pipeline_panel.refresh(self.pipeline_manager.pipeline)

    def remove_selected_step(self):
        idx = self.pipeline_panel.get_selected_index()
        self.pipeline_manager.remove_step(idx)
        self.pipeline_panel.refresh(self.pipeline_manager.pipeline)

    def move_selected_up(self):
        idx = self.pipeline_panel.get_selected_index()
        self.pipeline_manager.move_up(idx)
        self.pipeline_panel.refresh(self.pipeline_manager.pipeline)

    def move_selected_down(self):
        idx = self.pipeline_panel.get_selected_index()
        self.pipeline_manager.move_down(idx)
        self.pipeline_panel.refresh(self.pipeline_manager.pipeline)

    def run_pipeline(self):
        if self.image_manager.current is None:
            return
        self.image_manager.current = self.pipeline_manager.execute(
            self.image_manager.current,
            self.plugin_dict
        )
        self.update_views()

    def save_pipeline(self):
        path = filedialog.asksaveasfilename(defaultextension=".json")
        if path:
            self.pipeline_manager.save(path)

    def load_pipeline(self):
        path = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if path:
            self.pipeline_manager.load(path)
            self.pipeline_panel.refresh(self.pipeline_manager.pipeline)

    def clear_pipeline(self):
        self.pipeline_manager.clear()
        self.pipeline_panel.refresh(self.pipeline_manager.pipeline)

    def run_batch_pipeline(self):
        input_folder = filedialog.askdirectory(title="Input Folder")
        if not input_folder:
            return

        output_folder = filedialog.askdirectory(title="Output Folder")
        if not output_folder:
            return

        count = BatchProcessor.process_folder(
            input_folder,
            output_folder,
            self.pipeline_manager,
            self.plugin_dict
        )

        messagebox.showinfo(
            "Batch Complete",
            f"Processed {count} image(s)"
        )

    def save_image(self):
        if self.image_manager.current is None:
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png"
        )

        if path:
            self.image_manager.save(path)
