import {extend, ValidationProvider, ValidationObserver} from 'vee-validate';
import * as rules                                       from "vee-validate/dist/rules";
import Vue                                              from "vue";
import lang                                             from 'vee-validate/dist/locale/en.json';

Vue.component('ValidationProvider', ValidationProvider);
Vue.component('ValidationObserver', ValidationObserver);

Object.keys(rules).forEach((key) => {
    extend(key, {
        ...rules[key],
        message: lang.messages[key],
    });
});

extend('url', {
    validate(value) {
        const pattern = new RegExp('^(https?:\\/\\/)?' + // protocol
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
            '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
            '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
            '(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator
        return pattern.test(value);
    },
    message: 'Please enter a valid {_field_}.',
});
