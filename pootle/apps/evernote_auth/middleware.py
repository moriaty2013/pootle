#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Evernote Corporation
#
# This file is part of Pootle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from django.conf import settings


class NoCaptchaMiddleware:
    """Middleware to block displaying a captcha question to verify POST
    submissions are made by humans when linking with evernote.
    """
    def process_request(self, request):
        if not request.POST:
            return

        if (request.path.endswith('accounts/evernote/login/create') or
            request.path.endswith('accounts/evernote/login/create/')):

            settings.SAVED_USE_CAPTCHA = settings.USE_CAPTCHA
            settings.USE_CAPTCHA = False

            return
