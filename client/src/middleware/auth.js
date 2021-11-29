/**
 *
 * @param next
 * @param store
 * @returns {*}
 */
export default function auth({next, store}) {
    const auth = store.state.auth;
    const currentTime = Math.floor(Date.now() / 1000);
    const today = new Date(auth.user?.expired_time);
    try {
        if (!auth.user?.remember_token) {
            throw 'Missing access token!';
        }

        if (Math.floor(today / 1000) < currentTime) {
            store.commit('auth/setUser', null, {root: true});
            throw 'Token has expired!';
        }

        return next();
    } catch (error) {
        return next({name: 'login'});
    }
}
