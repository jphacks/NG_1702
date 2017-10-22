class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  helper_method :vapid_public_key

  def after_sign_in_path_for(resource)
    if resource.is_a?(User)
      user_ads_path
    else
      client_ads_path
    end
  end

  def vapid_public_key
    @decoded_vapid_public_key ||= Base64.urlsafe_decode64(ENV['WEB_PUSH_VAPID_PUBLIC_KEY']).bytes
  end
end
