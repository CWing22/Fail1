import FoxyVamp/bin
import FoxyVamp/cathy
import system.py

const Discord = require('discord.js');
const client = new Discord.Client();
 
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
 
client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
  }
});
 
client.login('NTQ2MTEzOTkzMDU2NTgzNjgw.D1yN0g.tTswuNKeuq_Ix-Ahp_38lebh_lk');
