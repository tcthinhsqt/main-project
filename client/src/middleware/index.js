import store from "../store";

export default class {
    /**
     *
     * @param context
     * @param middleware
     * @param index
     * @returns {(function(): void)|*}
     */
    middlewarePipeline(context, middleware, index) {
        const nextMiddleware = middleware[index]

        if (!nextMiddleware) {
            return context.next
        }

        return () => {
            const nextPipeline = this.middlewarePipeline(
                context, middleware, index + 1
            )
            nextMiddleware({...context, next: nextPipeline})
        }
    }

    /**
     *
     * @param to
     * @param from
     * @param next
     * @returns {*}
     */
    execute(to, from, next) {
        if (!to.meta.middleware) {
            return next()
        }

        const middleware = to.meta.middleware
        const context    = {
            to,
            from,
            next,
            store
        }

        return middleware[0]({
            ...context,
            next: this.middlewarePipeline(context, middleware, 1)
        })
    }
}
