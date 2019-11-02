from dotenv import load_dotenv
import os
import discord
load_dotenv()


class NoMaster(Exception):
    pass


class NoGuild(Exception):
    pass


class GuidManager:

    def __init__(self, guild=None, master_name=None):
        self.guild = guild
        self.master_name = os.getenv('DISCORD_MASTER')
        self.master_user = None
        self.top_dogs = []
        self.under_dogs = []
        self.slaves = []
        self.members = None
        if guild is not None:
            self.init(guild, master_name)

    def init(self, guild=None, master_name=None):
        """This method must be called before other functions are used."""
        if self.guild is None:
            if type(guild, discord.guild):
                self.guild = guild
            else:
                print("input guild is of wrong type")
                raise NoGuild

        self.members = self.guild.members
        self.set_master(master_name)

    def set_master(self, master_name=None):
        if master_name is not None:
            self.master_name = master_name
        master = self.check_master()
        if master is None:
            print(f"Error: master{self.master_name} not found in {self.guild.name}")
            raise NoMaster
        self.master_user = master

    def check_master(self):
        members = self.guild.members
        for member in members:
            if member.name == self.master_name:
                return member
        return None

    def add_top_dog(self, top_dog):
        for member in self.members:
            if type(top_dog, str):
                if member.name == top_dog:
                    self.top_dogs.append(member)
                    return True
            elif type(top_dog, member):
                if member == top_dog:
                    self.top_dogs.append(member)
                    return True
        return False

    def check_guild(self, guild):
        if guild != self.guild:
            return False
        return True

    def check_message_user(self, message):
        if message.author in self.top_dogs:
            return True
        return self.check_if_master()

    def check_if_master(self, user):
        if user == self.master_user:
            return True
        return False


    def save_guild(self):
        pass  # TODO: add json save the guild data.

    def load_guild(self):
        pass  # TODO: Load json guild data.
