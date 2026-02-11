import { app } from "/scripts/app.js";

app.registerExtension({
    name: "Comfy.ZNSUtils.BasicImageConfig",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "BasicImageConfig") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated
                    ? onNodeCreated.apply(this, arguments)
                    : undefined;

                this.addWidget("button", "🔄 Swap Dimensions", "swap", () => {
                    const widthWidget = this.widgets.find(
                        (w) => w.name === "base_width",
                    );
                    const heightWidget = this.widgets.find(
                        (w) => w.name === "base_height",
                    );

                    if (widthWidget && heightWidget) {
                        const temp = widthWidget.value;
                        widthWidget.value = heightWidget.value;
                        heightWidget.value = temp;
                    }
                });

                return r;
            };
        }
    },
});
