function closeModal(modalContainerId) {
	var container = document.getElementById(modalContainerId)
	var backdrop = container.getElementsByClassName("modal-backdrop")[0]
	var modal = container.getElementsByClassName("modal")[0]

	modal.classList.remove("show")
	backdrop.classList.remove("show")

	setTimeout(function() {
		container.removeChild(backdrop)
		container.removeChild(modal)
	}, 200)
}

function closeToast(toastId, toastContainerId='toast-container') {
	var container = document.getElementById(toastContainerId);
	var toastLive = document.getElementById(toastId);
	var toast = new bootstrap.Toast(toastLive);

	toast.hide(); // Hide the toast

	// Remove the toast from container
	if(container.childElementCount > 0){
		setTimeout(function () {
			container.removeChild(toastLive);
		}, 200);
	}
}

function showToast(toastId) {
	var toastLive = document.getElementById(toastId);
	var toast = new bootstrap.Toast(toastLive);

	toast.show(); // Show the toast
	
	// Destroy toast after being hidden
	toastLive.addEventListener('hidden.bs.toast', function () {
		closeToast(toastId);
	});
}

function handleErrorImage(elem) {
	elem.src = 'https://raw.githubusercontent.com/google/material-design-icons/master/src/image/broken_image/materialiconsround/24px.svg'
}