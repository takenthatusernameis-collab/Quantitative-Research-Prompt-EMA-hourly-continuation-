# EMA Hourly Continuation — T/USDT P50_55

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.2072 |
| net_win_rate | 0.3513 |
| gross_profit_factor | 0.7297 |
| gross_win_rate | 0.4278 |
| sharpe_ratio | -11.4941 |
| sortino_ratio | -4.4970 |
| max_drawdown | 0.9978 |
| cagr | -0.9104 |
| net_avg_win | 10.5169 |
| net_avg_loss | -27.4791 |
| avg_hold_time_bars | 3.3442 |
| exposure | 0.1068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
