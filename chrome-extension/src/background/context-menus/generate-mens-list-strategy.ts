/*
 * @Author: mulingyuer
 * @Date: 2024-11-01 17:16:56
 * @LastEditTime: 2024-11-05 16:23:27
 * @LastEditors: mulingyuer
 * @Description: 创建上下文菜单列表策略
 * @FilePath: \chrome-extension\src\background\context-menus\generate-mens-list-strategy.ts
 * 怎么可能会有bug！！！
 */
import type { ContextMenuStrategy } from "./types";
import { ContextMenuEnum } from "./context-menu-enum";
import { BaseMenu, ServerlessComfyuiMenu } from "./menus";
import type { CreateMenuOptions } from "@/utils/chrome-context-menus.ts";

/** 接收菜单数据并组合成list  */
function generateMenuList(...args: Array<CreateMenuOptions[]>): CreateMenuOptions[] {
	return ([] as CreateMenuOptions[]).concat(...args);
}

export const generateMensListStrategy: ContextMenuStrategy = {
	[ContextMenuEnum.CLEAR_ALL_BUSINESS_MENU]: () => {
		return generateMenuList(BaseMenu);
	},
	[ContextMenuEnum.CREATE_SERVERLESS_COMFYUI]: () => {
		return generateMenuList(BaseMenu, ServerlessComfyuiMenu);
	},
	[ContextMenuEnum.CREATE_SERVERLESS_SDXL_TEXT2IMG]: () => {
		return generateMenuList(BaseMenu, ServerlessComfyuiMenu);
	}
};
