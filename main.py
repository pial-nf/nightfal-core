# READ ALL THE -> # <- ONES IF YOU DON'T KNOW WHAT THAT COMMAND DOES
import os
import discord
from itertools import cycle
from discord.ext import commands, tasks
from discord.gateway import DiscordWebSocket

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='<', case_insensitive=True, intents=intents, help_command=None)
status = cycle(['Devloper', "Pial Mallik", "NightFall", 'prefix ( < )'])

@client.event
async def on_ready():
  change_status.start()
  print('Bot is online!')

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(status=discord.Status , activity=discord.Game(next(status)))

# MOBILE STATUS
class MyDiscordWebSocket(DiscordWebSocket):

    async def send_as_json(self, data):
        if data.get('op') == self.IDENTIFY:
            if data.get('d', {}).get('properties', {}).get('$browser') is not None:
                data['d']['properties']['$browser'] = 'Discord Android'
                data['d']['properties']['$device'] = 'Discord Android'
        await super().send_as_json(data)

DiscordWebSocket.from_client = MyDiscordWebSocket.from_client

# HELP COMMAND
@client.group(invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(
        title="**FrenZ | Help Panel**",
        description=f"**Use `{client.command_prefix}help <module> or <command>` to extend information of a command**",
        color = 0x050505
    )
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Developed by VibE<₹#1337 | Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="__**Modules**__", value = "Information \n Moderation \n Antinuke", inline=False)
    embed.add_field(name="Links", value = "[Support Server](https://discord.gg/nightcafe)", inline=False)
    await ctx.reply(embed=embed)

@help.command()
async def information(ctx):
    embed=discord.Embed(
        title="**FrenZ | Information**",
        description="`ping`, `membercount`, `serverinfo`, `userinfo`, `checkprune`",
        color = 0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def moderation(ctx):
    embed=discord.Embed(
        title="**FrenZ | Moderation**",
        description="`kick`, `ban`, `unban`, `unbanall`, `addrole`, `removerole`, `warn`, `slowmode`, `setnick`, `createchannel`, `deletechannel`, `createrole`, `deleterole`, `hide`, `unhide`, `lock`, `unlock`, `clear`, `drag`, `move`, `prune`, `nuke`",
        color = 0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def antinuke(ctx):
    embed=discord.Embed(
        title="**FrenZ | Antinuke**",
        description="""`Anti Bot Add`,
`Anti Kick`,
`Anti Ban`,
`Anti Unban`,
`Anti Prune`,
`Anti Channel Delete`,
`Anti Channel Create`,
`Anti Channel Update`,
`Anti Guild Update`,
`Anti Member Update`,
`Anti Mentioning`,
`Anti Role Create`,
`Anti Role Delete`,
`Anti Role Update`,
`Anti Emoji Create`,
`Anti Emoji Delete`,
`Anti Emoji Update`,
`Anti Webhook Create`,
`Anti Webhook Delete`,
`Anti Webhook Update`""",
        color = 0x050505
    )
    embed.add_field(name="Whitelisted User", value="Respected Guild Owner<₹")
    await ctx.reply(embed=embed)
    

@help.command()
async def ping(ctx):
    embed=discord.Embed(
        title="Ping",
        description="`Shows the latency of the bot.`",
        color = 0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def membercount(ctx):
    embed=discord.Embed(
        title="Membercount",
        description="`Shows the count of members in the server.`",
        color = 0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def serverinfo(ctx):
    embed=discord.Embed(
        title="SevrerInfo",
        description="`Shows the information of the server",
        color = 0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def userinfo(ctx):
    embed=discord.Embed(
        title="UserInfo",
        description="`Shows the information of a member`",
        color = 0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def checkprune(ctx):
    embed=discord.Embed(
        title="CheckPrune",
        description="`Shows the number of members prunable.`",
        color=0x050505
    )
    await ctx.reply(embed=embed)

@help.command()
async def kick(ctx):
    embed=discord.Embed(
        title="Kick",
        description="`Kicks the specified member from the server.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹kick [member] {reason}`")
    await ctx.reply(embed=embed)

@help.command()
async def ban(ctx):
    embed=discord.Embed(
        title="Ban",
        description="`Bans the specified member from the server.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹ban [member] {reason}`")
    await ctx.reply(embed=embed)

@help.command()
async def unban(ctx):
    embed=discord.Embed(
        title="Unban",
        description="`Unbans the specified member from the server.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹unban [member]`")
    await ctx.reply(embed=embed)

@help.command(aliases=['ar'])
async def addrole(ctx):
    embed=discord.Embed(
        title="AddRole",
        description="`Adds a specified role to the mentioned member.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹addrole [member] [role]`")
    embed.add_field(name="Aliases", value="`ar`")
    await ctx.reply(embed=embed)

@help.command(aliases=['rr'])
async def removerole(ctx):
    embed=discord.Embed(
        title="RemoveRole",
        description="`Removes a specified role from the mentioned member.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹removerole [member] [role]`")
    embed.add_field(name="Aliases", value="`rr`")
    await ctx.reply(embed=embed)

@help.command()
async def warn(ctx):
    embed=discord.Embed(
        titile="Warn",
        description="`Warns a mentioned user for a specified reason.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹warn [member] [reason]`")
    await ctx.reply(embed=embed)

@help.command()
async def slowmode(ctx):
    embed=discord.Embed(
        title="SlowMode",
        description="`Sets the channel's slowmode speed to specified seconds.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹slowmode [seconds]`")
    await ctx.reply(embed=embed)

@help.command(aliases=['nick'])
async def setnick(ctx):
    embed=discord.Embed(
        titile="SetNick",
        description="`Sets the mentioned member's nickname to the specified nick`.",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹setnick [member] [nickname]`")
    embed.add_field(name="Aliases", value="`nick`")
    await ctx.reply(embed=embed)

@help.command(aliases=['cc'])
async def createchannel(ctx):
    embed=discord.Embed(
        title="CreateChannel",
        description="`Creates a channel with the name specified.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹createchannel [name]`")
    embed.add_field(name="Aliases", value="`cc`")
    ctx.reply(embed=embed)

@help.command(aliases=['dc', 'delchannel'])
async def deletechannel(ctx):
    embed=discord.Embed(
        title="DeleteChannel",
        description="`Deletes a mentioned channel.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹deletechannel [channel]`")
    embed.add_field(name="Aliases", value="`dc`, `delchannel`")
    await ctx.reply(embed=embed)

@help.command(aliases=['cr'])
async def createrole(ctx):
    embed=discord.Embed(
        title="CreateRole",
        description="`Creates a role with the name specified.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹createrole [name]`")
    embed.add_field(name="Aliases", value="`cr`")
    await ctx.reply(embed=embed)

@help.command(aliases=['dr', 'delrole'])
async def deleterolerole(ctx):
    embed=discord.Embed(
        title="DeleteRole",
        description="`Deletes the specified role`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹deleterole [role-name]`")
    embed.add_field(name="Aliases", value="`dr`, `delrole`")
    await ctx.reply(embed=embed)

@help.command()
async def hide(ctx):
    embed=discord.Embed(
        title="Hide",
        description="`Hides the channel from @everyone.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`hide`")
    await ctx.reply(embed=embed)

@help.command()
async def unhide(ctx):
    embed=discord.Embed(
        title="Unhide",
        description="`Unhides the channel for @everyone.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹unhide`")
    await ctx.reply(embed=embed)

@help.command()
async def lock(ctx):
    embed=discord.Embed(
        title="Lock",
        description="`Locks the channel.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹lock`")
    await ctx.reply(embed=embed)

@help.command()
async def unlock(ctx):
    embed=discord.Embed(
        title="Unlock",
        description="`Unlocks the channel.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹unlock`")
    await ctx.reply(embed=embed)

@help.command(aliases=['purge', 'del', 'delete'])
async def clear(ctx):
    embed=discord.Embed(
        title="Clear",
        description="`Clears the amount of messages.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹clear [amount_of_messages]`")
    embed.add_field(name="Aliases", value="`purge`, `del`, `delete`")
    await ctx.reply(embed=embed)

@help.command()
async def drag(ctx):
    embed=discord.Embed(
        title="Drag",
        description="`Drags a user from one vc to another.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹drag [user] [voicechannel]`")
    await ctx.reply(embed=embed)

@help.command()
async def move(ctx):
    embed=discord.Embed(
        title="Move",
        description="`Moves the mentioned role's members from a vc to another.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹move [role] [vc]`")
    await ctx.reply(embed=embed)

@help.command()
async def prune(ctx):
    embed=discord.Embed(
        title="Prune",
        description="`Prunes members according to the number of days specified.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹prune 1`")
    await ctx.reply(embed=embed)

@help.command()
async def nuke(ctx):
    embed=discord.Embed(
        title="Nuke",
        description="`Nukes the channel.`",
        color = 0x050505
    )
    embed.add_field(name="Usage", value="`₹nuke`")
    await ctx.reply(embed=embed)







# COMMAND ERROR
@client.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    await ctx.reply(embed=discord.Embed(color=0x050505, title="Error!", description=f'```{error}```'))

# PING
@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong! {round(client.latency * 1000)}ms.")

# KICK
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member,*,reason="Action issued by an admin"):
  embed = discord.Embed(
    title = 'Done!',
    description = f"**Successfully kicked {member.mention}!**", color = 0x050505
  )
  embed.set_footer(text=f"Action taken by {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
  await member.kick(reason=f"FrenZ | {reason}")
  await ctx.send(embed=embed)

# BAN
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member,*,reason="Action issued by an admin"):
  embed = discord.Embed(
    title = 'Done!',
    description = f"**Successfully banned {member.mention}!**", color = 0x050505
  )
  embed.set_footer(text=f"Action taken by {ctx.author.name}", icon_url=ctx.author.avatar_url)
  
  await member.ban(reason=f"FrenZ | {reason}")
  await ctx.send(embed=embed)

# UNBAN
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user, reason="FrenZ | Action issued by an admin")
      await ctx.send(f'**Successfully unbanned** {user.mention} !')
      return

# ADD ROLE
@client.command(aliases=['ar'])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
  embed=discord.Embed(
    title = "Done!",
    description = f"**Successfully added `{role.name}` to {member.mention}!**",
    color = 0x050505
  )
  embed.set_footer(text=f"Action taken by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
  await member.add_roles(role, reason=f"FrenZ | Action taken by a mod")
  await ctx.send(embed=embed)

# REMOVE ROLE
@client.command(aliases=['rr'])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
  embed=discord.Embed(
    title = "Done!",
    description = f"**Successfully removed `{role.name}` from {member.mention}!**",
    color = 0x050505
  )
  embed.set_footer(text=f"Action taken by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)
  await member.remove_roles(role, reason=f"FrenZ | Action taken by a mod")
  await ctx.send(embed=embed)

# WARN
@client.command()
async def warn(ctx, member: discord.Member, *, reason=None):
  if ctx.author.guild_permissions.manage_roles:
    mbed=discord.Embed(
      title="Warning!",
      description=f"{member.mention} **has been warned !** \n **Reason**: `{reason}`",
      color = 0x050505
        )
    mbed.set_footer(text=f"Action taken by {ctx.author.name}")
    mbed2=discord.Embed(title="Warning!", description=f"**You were warned in `{ctx.guild.name}` for `{reason}`**", color = 0x050505)
    await ctx.send(embed=mbed)
    await member.send(embed=mbed2)

# SLOW MODE
@client.command()
async def slowmode(ctx, seconds: int):
  if ctx.author.guild_permissions.manage_channels:
    mbed=discord.Embed(title="Done!", description=f"**Successfully set the slowmode of the channel to {seconds}seconds!**", color = 0x050505)
    mbed.set_footer(text=f"Action taken by {ctx.author.name}")
    await ctx.channel.edit(slowmode_delay=seconds, reason="FrenZ | Action issued by an admin")
    await ctx.send(embed=mbed)

#### SETNICK

@client.command(pass_content=True, aliases=['nick'])
async def setnick(ctx, member: discord.Member, *, nick):
  mbed = discord.Embed(title = "Done!",
                      description = f"*Nickname has been changed for {member.mention} !**", color = 0x050505)
  mbed.set_footer(text=f"Action taken by {ctx.author.name}", icon_url=ctx.author.avatar_url)
  if ctx.author.guild_permissions.manage_nicknames:
   await member.edit(nick=nick, reason="FrenZ | Action issued by a mod")
   await ctx.send(embed=mbed)

# CREATE CHANNNEL
@client.command(aliases=['cc'])
async def createchannel(ctx, channelName):
  guild = ctx.guild
  embed=discord.Embed(title="Done!", description="**Successfully created {} **".format(channelName), color = 0x050505)
  embed.set_footer(text=f"Action taken by {ctx.author.name}")
  if ctx.author.guild_permissions.manage_channels:
      
    await guild.create_text_channel(name='{}'.format(channelName), reason="FrenZ | Action issued by an admin")
    await ctx.send(embed=embed)

# DELETE CHANNEL
@client.command(aliases=['dc', 'delchannel'])
async def deletechannel(ctx, channel: discord.TextChannel):
  embed=discord.Embed(title="Done!", description=f"**Successfully deleted {channel}**", color = 0x050505)
  embed.set_footer(text=f"Action taken by {ctx.author.name}")
  if ctx.author.guild_permissions.manage_channels:
    await channel.delete(reason="FrenZ | Action issued by an admin")
    await ctx.send(embed=embed)

# CREATE ROLE
@client.command(aliases=['cr'])
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, *,name):
  guild = ctx.guild
  embed = discord.Embed(
    title = 'Done!', 
    description = f"**Role {name} has been successfully created by {ctx.author.name}**", color = 0x050505)
  await guild.create_role(name=name, reason="FrenZ | Action issued by an admin")
  await ctx.send(embed=embed)

# DELETE ROLE
@client.command(aliases=['dr', 'deleterole'])
@commands.has_permissions(manage_roles=True)
async def delrole(ctx,*, role_name):
  role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
  embed = discord.Embed(
    title = 'Done!', 
    description = f"**Role {role_name} has been successfully deleted by {ctx.author.name}**", color = 0x050505)
  await role_object.delete(reason="FrenZ | Action issued by an admin")
  await ctx.send(embed=embed)


# HIDE
@client.command(aliases=['hidechannel'])
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel=None):
  overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
  overwrite.read_messages = False
  embed=discord.Embed(title="Done!", description=f"<#{ctx.channel.id}> **is now hidden from everyone**", color = 0x050505)
  await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason="FrenZ | Action issued by an admin")
  await ctx.send(embed=embed)

# UNHIDE
@client.command(aliases=['unhidechannel'])
async def unhide(ctx, channel: discord.TextChannel=None):
  overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
  overwrite.read_messages = True
  embed=discord.Embed(title="Done!", description=f"<#{ctx.channel.id}> **is now visible to everyone**", color = 0x050505)
  if ctx.author.guild_permissions.manage_channels:
      
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason="FrenZ | Action issued by an admin")
    await ctx.send(embed=embed)

# LOCK
@client.command(aliases=['lockchannel'])
async def lock(ctx, channel: discord.TextChannel=None):
  overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  embed=discord.Embed(title="Done!", description=f"<#{ctx.channel.id}> **has been locked by {ctx.author.name})**", color =0x050505)
  if ctx.author.guild_permissions.manage_channels:
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason="FrenZ | Action issued by an admin")
    await ctx.send(embed=embed)

# UNLOCK
@client.command(aliases=['unlockchannel'])
async def unlock(ctx, channel: discord.TextChannel=None):
  overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  embed=discord.Embed(title="Done!", description=f"<#{ctx.channel.id}> **has been unlocked by {ctx.author.name})**", color =0x050505)
  if ctx.author.guild_permissions.manage_channels:
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason="FrenZ | Action issued by an admin")
    await ctx.send(embed=embed)

# SERVERINFO
@client.command(aliases=['si'])
async def serverinfo(ctx):
  mbed = discord.Embed(title="Server information", color = 0x050505)
  mbed.add_field(name="**Server Name**", value=f"`{ctx.message.guild.name}`", inline=False)
  mbed.add_field(name="**Roles**", value=f"`{len(ctx.message.guild.roles)}`", inline=False)
  mbed.add_field(name="**Members**", value=f"`{len(ctx.message.guild.members)}`", inline=False)
  mbed.add_field(name="**Channels**", value=f"`{len(ctx.message.guild.channels)}`", inline=False)
  mbed.add_field(name="**Region**", value=f"`{ctx.message.guild.region}`", inline=False)
  mbed.add_field(name="**Verification Level**",value=f"`{str(ctx.guild.verification_level)}`",inline=False)
  mbed.add_field(name="**Highest Role**",value=f"`{ctx.guild.roles[-1]}`",inline=False)
  mbed.set_footer(text=f"Requested by {ctx.author}")
  mbed.set_thumbnail(url=ctx.author.guild.icon_url)
  await ctx.send(embed=mbed)

# USERINFO
@client.command(aliases=['ui', 'whois'])
async def userinfo(ctx, member: discord.Member=None):
  if member == None:
    member = ctx.author
  roles = [role for role in member.roles]
  mbed = discord.Embed(color = 0x050505, timestamp = ctx.message.created_at)
  mbed.set_author(name=f"UserInfo - {member}")
  mbed.set_thumbnail(url=ctx.author.avatar_url)
  mbed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  mbed.add_field(name="ID:", value=member.id, inline=False)
  mbed.add_field(name="Username:", value=member.name, inline=False)
  mbed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
  mbed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
  mbed.add_field(name=f"Roles ({len(roles)}):", value=" ".join([role.mention for role in roles]), inline=False)
  mbed.add_field(name="Top Role:", value=member.top_role.mention, inline=False)
  mbed.add_field(name="Bot?", value=member.bot, inline=False)

  await ctx.send(embed=mbed)

# PRUNE
@client.command()
@commands.has_permissions(administrator=True)
async def prune(ctx , days :int):
  embed=discord.Embed(title="Done!", description="Successfully pruned members!", color=0x050505)
  if ctx.author.guild_permissions.administrator:
    await ctx.guild.prune_members(days= days, compute_prune_count=False, roles=ctx.guild.roles)
    await ctx.reply(embed=embed)

# CHECK PRUNE
@client.command(aliases=['cp'])
async def checkprune(ctx,days: int):
  guild = ctx.guild
  po = await ctx.guild.estimate_pruned_members(days=days, roles=guild.roles)
  if ctx.author.guild_permissions.ban_members:
    await ctx.reply(f"{po} members will get pruned for being inactive for {days} days.")

# LOGOUT
@client.command(aliases=["logout"])
async def shutdown(ctx):
  if ctx.author.id == 954412450428620880:
    await ctx.reply("Logging out...")
    await ctx.reply("Successfully logged out !")
    await client.logout()

# NUKE
@commands.has_permissions(administrator=True)
@client.command(aliases=['nuke'])
@commands.cooldown(1, 15, commands.BucketType.guild)
async def clone(ctx):
        channelthings = [ctx.channel.category, ctx.channel.position]
        await ctx.channel.clone()
        await ctx.channel.delete()
        embed=discord.Embed(title=f'Nuked Channel!', description=f'**Channel was nuked by {ctx.author.name}**',color=0x2f3136, timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/972408873635966986/976370702489890847/1289.png")
        nukedchannel = channelthings[0].text_channels[-1]
        await nukedchannel.edit(position=channelthings[1])
        await nukedchannel.send(embed=embed)

# MEMBERCOUNT
@client.command(aliases=['mc'])
async def membercount(ctx):
  user_count = len([x for x in ctx.guild.members if not x.bot])
  online = len(list(filter(lambda m: str(m.status)=="online", ctx.guild.members)))
  idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
  dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
  offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
  t_online = [online, idle, dnd]
  Sum = sum(t_online)
  mbed=discord.Embed(title="Membercount", description=f"**Total Members = {ctx.author.guild.member_count} \n Users = {user_count} \n Bots = {ctx.author.guild.member_count - user_count} \n Total Online = {Sum} \n Online status = {online} \n Idle status = {idle} \n Dnd status = {dnd} \n Offline = {offline}**", color=0x2f3136)
  mbed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=mbed)

# DRAG
@client.command()
@commands.has_permissions(administrator=True)
async def drag(ctx, member: discord.Member, channel: discord.VoiceChannel):
  await member.move_to(channel, reason="FrenZ | Action taken by a mod")
  await ctx.reply(f"Moved {member.display_name} to `{channel.name}` !")

# MOVE
@client.command()
@commands.has_permissions(administrator=True)
async def move(ctx, givenRole: discord.Role, channel: discord.VoiceChannel):
  for member in givenRole.members:
    try:
      await member.move_to(channel, reason="FrenZ | Action taken by a mod")
      await ctx.reply(f"**{member.display_name}** moved to `{channel.name}`")
    except:
      await ctx.reply("Couldn't...")

###################### ANTI NUKE

# ANTI BOT
@client.event
async def on_member_join(member):
    guild = member.guild
    reason = "FrenZ | Anti-Bot-Add"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
    logs = logs[0]
    if member.bot:
        if logs.user == guild.owner:
            pass
        else:
            await member.ban(reason=f"{reason}")
            await logs.user.ban(reason=f"{reason}")

# ANTI KICK
@client.event
async def on_member_kick(guild, member):
    guild = member.guild
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
    logs = logs[0]
    reason = "FrenZ | Kicking Members"
    if logs.user == guild.owner:
        pass
    else:
        await logs.user.ban(reason=f"{reason}")

# ANTI PRUNE
@client.event
async def on_member_remove(guild, member):
  guild = member.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.member_prune).flatten()
  logs = logs[0]
  reason = "FrenZ | Anti Prune"
  if logs.user == guild.owner:
      pass
  else:
      await logs.user.ban(reason=f"{reason}")

# ANTI BAN
@client.event
async def on_member_ban(guild, member : discord.Member):
    reason = "FrenZ | Anti-Ban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    logs = logs[0]
    if logs.user == guild.owner:
        pass
    else:
      await logs.user.ban(reason=f"{reason}")
      await guild.unban(user=member, reason=f"{reason}")

# ANTI UNBAN
@client.event
async def on_member_unban(guild, member : discord.Member):
    reason = "FrenZ | Anti-Unban"
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.unban).flatten()
    logs = logs[0]
    if logs.user == guild.owner:
        pass
    else:
      await logs.user.ban(reason=f"{reason}")

# ANTI CHANNEL DELETE
@client.event
async def on_guild_channel_delete(channel):
  reason = "FrenZ | Anti Channel Delete"
  guild = channel.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")
  if logs.user == guild.owner:
    pass
  else:
    if isinstance(channel, discord.TextChannel):
        await guild.create_text_channel(channel.name, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
    if isinstance(channel, discord.VoiceChannel):
        await guild.create_voice_channel(f"{channel}")

# ANTI GUILD UPDATE
@client.event
async def on_guild_update(before, after, guild):
  reason = "FrenZ | Anti Guild Update"
 # guild = after.guild
  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")
    await after.edit(name=f"{before.name}")

# ANTI MEMBER UPDATE
@client.event
async def on_member_update(before, after, guild):
  reason = "FrenZ | Anti Member Update"
  logs = await before.guild.audit_logs(limit=1,action=discord.AuditLogAction.member_role_update).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason = f"{reason}")

# ANTI CHANNEL CREATE
@client.event
async def on_guild_channel_create(ch, guild):
    try:
        async for entry in ch.guild.audit_logs(limit = 1 , action = discord.AuditLogAction.channel_create):
            if entry.user == guild.owner:
              pass
            else:
              await ch.guild.ban(entry.user , reason = "FrenZ | Anti Channel")
              await ch.delete()
    except Exception as e:
        print(e)

# ANTI PING
@client.event
async def on_message(message):
  await client.process_commands(message)
  member = message.author
  guild = message.guild
  if message.mention_everyone:
    if member == guild.owner:
      pass
    else:
      await message.delete()
      await member.kick(reason="FrenZ | Mentioning everyone/here")

# ANTI ROLE CREATE
@client.event
async def on_guild_role_create(role):
  reason = "FrenZ | Anti Role Create"
  guild = role.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")
    await role.delete()

# ANTI ROLE DELETE
@client.event
async def on_guild_role_delete(role):
  guild = role.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
  reason = "FrenZ | Anti Role Delete"
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")
    await guild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)

# ANTI EMOJI CREATE
@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_create).flatten()
  reason = "FrenZ | Anti Emoji Create"
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")
    await guild.emoji_delete()

# ANTI EMOJI DELETE
@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_delete).flatten()
  reason = "FrenZ | Anti Emoji Delete"
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")

# ANTI EMOJI UPDATE
@client.event
async def on_guild_emojis_update(guild, before, after):
  #guild = emoji.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_update).flatten()
  reason = "VibE | Anti Emoji Update"
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")

# ANTI ROLE UPDATE
@client.event
async def on_guild_role_update(before, after):
  reason = "FrenZ | Anti Role Update"
  guild = after.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")

# ANTI CHANNEL UPDATE
@client.event
async def on_guild_channel_update(before, after):
  reason = "FrenZ | Anti Channel Update"
  guild = after.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")

# ANTI WEBHOOK CREATE
@client.event
async def on_webhook_update(webhook):
  reason = "FrenZ | Anti Webhook Create"
  guild = webhook.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
  logs = logs[0]
  if logs.user == guild.owner:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")

# ANTI WEBHOOK DELETE
@client.event
async def on_webhooks_update(webhook):
  reason = "FrenZ | Anti Webhook Delete"
  guild = webhook.guild
  logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_delete).flatten()
  logs = logs[0]
  if logs.user.id in wl:
    pass
  else:
    await logs.user.ban(reason=f"{reason}")

# ANTI WEBHOOK UPDATE
@client.event
async def on_webhook_update(webhook):
    reason="FrenZ | Anti Webhook Update"
    guild = webhook.guild
    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_update).flatten()
    logs = logs[0]
    if logs.user == guild.owner:
        pass
    else:
        await logs.user.ban(reason=f"{reason}") 

######################


client.run("MTMzNDIxMDQ5NTE2NjU0NTk1MA.GsQvzj.hq_08tPo7GnvFjOuWmZjTzLHDTCsqH4Bxu1slo")