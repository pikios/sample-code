# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

key = @client.preview.deployed_devices
                     .fleets('FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                     .keys('KYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                     .update(friendly_name: 'friendly_name')

puts key.friendly_name
