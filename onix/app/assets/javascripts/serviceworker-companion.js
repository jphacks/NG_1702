if (navigator.serviceWorker) {
    navigator.serviceWorker.register('/serviceworker.js', {scope: '/'})
        .then(function (reg) {
            console.log('[Page] Service worker registered!');

            /*
             // プッシュ通知の購読
             reg.pushManager.subscribe({
             userVisibleOnly: true,
             applicationServerKey: window.vapidPublicKey
             }).then(subscribeSuccess);
             */
            return reg.pushManager.getSubscription().then(function (subscription) {
                if (subscription) {
                    return subscription
                }
                return reg.pushManager.subscribe({
                    userVisibleOnly: true
                })
            })
        }).then(function (subscription) {
        subscribeSuccess(subscription)
    })
}

var subscribeSuccess = function (subscription) {
    var tmp = subscription.toJSON();
    params = {
        subscription: {
            endpoint: tmp.endpoint,
            auth: tmp.keys.auth,
            p256dh: tmp.keys.p256dh,
        }
    };
    console.log(params);

    $.ajaxPrefilter(function(options, originalOptions, jqXHR) {
        var token;
        if (!options.crossDomain) {
            token = $('meta[name="csrf-token"]').attr('content');
            if (token) {
                return jqXHR.setRequestHeader('X-CSRF-Token', token);
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: '/devices',
        data: params
    });
};