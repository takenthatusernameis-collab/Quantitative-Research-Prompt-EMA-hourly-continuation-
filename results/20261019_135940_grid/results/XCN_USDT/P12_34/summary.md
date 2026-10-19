# EMA Hourly Continuation — XCN/USDT P12_34

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1503 |
| net_profit_factor | 0.3524 |
| net_win_rate | 0.3799 |
| gross_profit_factor | 0.6804 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -13.0868 |
| sortino_ratio | -7.1781 |
| max_drawdown | 0.9999 |
| cagr | -0.9744 |
| net_avg_win | 9.5304 |
| net_avg_loss | -16.5674 |
| avg_hold_time_bars | 3.7964 |
| exposure | 0.2594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
