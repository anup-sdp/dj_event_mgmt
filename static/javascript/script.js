const dialog = document.querySelector("#dialog1");

function openDialog() {      
	//dialog.show(); // Opens a non-modal dialog
	dialog.showModal();
}

function closeDialog() {      
	dialog.close();
}   

dialog.addEventListener('click', (event) => {
	// When opened via showModal(), clicking on backdrop yields event.target === dialog
	if (event.target === dialog) {
	  dialog.close();
	}
});

function dismissMessage(btn) {
	const msgEl = btn.closest('.message'); // climbs up through its(btn) ancestors - closest() vs parentElement
	msgEl.classList.add('fade-out');
	// After transition, remove from DOM
	msgEl.addEventListener('transitionend', () => {
		msgEl.remove();
	}, { once: true });
}