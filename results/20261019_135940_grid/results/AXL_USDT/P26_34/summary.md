# EMA Hourly Continuation — AXL/USDT P26_34

**Symbol:** AXL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1133 |
| net_profit_factor | 0.3637 |
| net_win_rate | 0.3742 |
| gross_profit_factor | 0.8419 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -12.0715 |
| sortino_ratio | -5.7784 |
| max_drawdown | 0.9994 |
| cagr | -0.9487 |
| net_avg_win | 13.4730 |
| net_avg_loss | -22.1537 |
| avg_hold_time_bars | 2.4581 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
