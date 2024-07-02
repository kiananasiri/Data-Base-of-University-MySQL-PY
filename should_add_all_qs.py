rows = execute_query(query)
    if rows:
        show_results_page(rows)  # Call function to show results
    else:
        print("No results found.")  # Handle case where no rows are returned

def show_results_page(rows):
    # Create a new widget to display the results
    results_page = QWidget()
    layout = QVBoxLayout(results_page)

    # Add widgets to display the results (e.g., QLabel, QTableWidget, etc.)
    result_label = QLabel("Results for Q1:")
    layout.addWidget(result_label)

    # Example: Display results in a QTableWidget
    table = QTableWidget()
    table.setColumnCount(1)  # Adjust column count as per your data
    table.setRowCount(len(rows))
    table.setHorizontalHeaderLabels(["Student Enrollment ID"])  # Adjust header labels

    for row_index, row in enumerate(rows):
        table.setItem(row_index, 0, QTableWidgetItem(str(row[0])))

    layout.addWidget(table)

    # Add the layout to the widget
    results_page.setLayout(layout)

    # Add results_page to stacked widget and set as current widget
    form.stacked_widget.addWidget(results_page)
    form.stacked_widget.setCurrentWidget(results_page)
