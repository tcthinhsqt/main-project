import {v4 as uuidv4} from 'uuid';

/**
 * ページタイトル生成
 * @param {Object} route
 * @returns {string}
 */
export const generatePageTitle = (route) => {
    const separator = '｜';
    return [(route?.meta?.title ?? ''), process.env.MIX_APP_NAME]
        .filter(v => v)
        .join(separator);
};

/**
 * Generate uuid for the first access
 * @returns {string}
 */
export const generateUUID = () => {
    return uuidv4();
};
