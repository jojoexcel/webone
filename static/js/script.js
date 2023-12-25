function deletePersonnel() {
    if (confirm('Are you sure you want to delete this personnel record?')) {
        // Redirect to the delete route when confirmed
        console.log("Delete URL:", "{{ url_for('delete_personnel', personnel_id=personnel[0]) }}");
        window.location.href = "{{ url_for('delete_personnel', personnel_id=personnel[0]) }}";
    }
}