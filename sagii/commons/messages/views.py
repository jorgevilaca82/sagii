from django.contrib import messages


class SuccessMessageOnDeleteMixin(object):
    """
    Add a success message on successful form delete submission.
    """
    success_message = ''

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        success_message = self.get_success_message(obj)
        if success_message:
            messages.success(request, success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_message(self, obj):
        return self.success_message % obj.__dict__
