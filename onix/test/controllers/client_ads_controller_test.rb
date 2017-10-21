require 'test_helper'

class ClientAdsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get client_ads_index_url
    assert_response :success
  end

end
