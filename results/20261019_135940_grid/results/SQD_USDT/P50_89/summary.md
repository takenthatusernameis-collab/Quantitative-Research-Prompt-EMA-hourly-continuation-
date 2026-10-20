# EMA Hourly Continuation — SQD/USDT P50_89

**Symbol:** SQD/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6638 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0654 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -3.8950 |
| sortino_ratio | -1.3662 |
| max_drawdown | 0.8077 |
| cagr | -0.4885 |
| net_avg_win | 52.9012 |
| net_avg_loss | -77.1197 |
| avg_hold_time_bars | 4.9377 |
| exposure | 0.1416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
