/**
 *
 * @param next
 * @param store
 * @returns {*}
 */
export default function auth({next, store}) {
    const auth = store.state.auth;
    const currentTime = Math.floor(Date.now() / 1000);

    try {
        if (!auth.user?.remember_token) {
            throw 'Missing access token!';
        }

        if (Math.floor(auth.user?.expired_time / 1000) < currentTime) {
            throw 'Token has expired!';
        }
        return next();
    } catch (error) {
        return next({name: 'login'});
    }
}
