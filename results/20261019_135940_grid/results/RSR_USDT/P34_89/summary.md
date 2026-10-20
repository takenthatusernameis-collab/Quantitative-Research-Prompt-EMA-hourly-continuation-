# EMA Hourly Continuation — RSR/USDT P34_89

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6394 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -4.1412 |
| sortino_ratio | -1.4955 |
| max_drawdown | 0.8472 |
| cagr | -0.5141 |
| net_avg_win | 47.7049 |
| net_avg_loss | -66.1071 |
| avg_hold_time_bars | 8.0619 |
| exposure | 0.2426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
