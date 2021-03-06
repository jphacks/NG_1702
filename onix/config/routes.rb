Rails.application.routes.draw do

  devise_for :clients, controllers: {
      sessions:      'clients/sessions',
      passwords:     'clients/passwords',
      registrations: 'clients/registrations'
  }
  devise_for :users, controllers: {
      sessions:      'users/sessions',
      passwords:     'users/passwords',
      registrations: 'users/registrations'
  }
  root 'top#index'
  resources  :user_ads, only: %i(index show) do
    get 'post', :on => :collection
    get 'setting', :on => :collection
    get 'coin', :on => :collection
    get 'get_ad', :on => :member
  end

  resources  :client_ads, only: %i(index new create) do
    get 'setting', :on => :collection
    get 'check', :on => :member
  end
  get 'top/index' => 'top#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  resources :devices, only: [:create]
end
