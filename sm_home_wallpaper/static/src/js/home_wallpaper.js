/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { onWillStart } from "@odoo/owl";
import { HomeMenu } from "@web_enterprise/webclient/home_menu/home_menu";

patch(HomeMenu.prototype, "sm_home_wallpaper", {
    setup() {
        super.setup(...arguments);
        this.orm = useService("orm");
        onWillStart(async () => {
            try {
                const attachmentId = await this.orm.call(
                    "res.config.settings",
                    "sm_get_random_wallpaper"
                );
                if (attachmentId) {
                    const url = `/web/image/${encodeURIComponent(attachmentId)}`;
                    document.body.style.setProperty(
                        "--homeMenu-bg-image",
                        `url("${url}")`
                    );
                    document.body.classList.add("o_home_menu_background_custom");
                }
            } catch {
                // Silently ignore — wallpaper is not critical
            }
        });
    },
});
