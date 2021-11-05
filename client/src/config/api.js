/*
|--------------------------------------------------------------------------
| APIに関する設定
|--------------------------------------------------------------------------
*/

import {trimEnd} from 'lodash';

export default {
    internal: {
        baseUrl: trimEnd(process.env.MIX_API_SERVER, '/'),
    },
};
