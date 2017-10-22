class WebpushService
  def initialize(user_id: nil)
    @user_id = user_id
  end

  def webpush_clients(message)
    devices.each do |device|
      webpush device, message
      binding.pry
    end
  end

  def webpush(device, message)
    Webpush.payload_send(
        message: message,
        endpoint: device.endpoint,
        p256dh: device.p256dh,
        auth: device.auth,
        ttl: 24 * 60 * 60,
        vapid: {
            public_key: ENV['WEB_PUSH_VAPID_PUBLIC_KEY'],
            private_key: ENV['WEB_PUSH_VAPID_PRIVATE_KEY']
        }
    )
  end

  private

  def devices
    @user_id.present? ? Device.where(user_id: @user_id) : Device.all
  end
end