# EMA Hourly Continuation — JTO/USDT P8_89

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.6379 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -3.9257 |
| sortino_ratio | -1.4576 |
| max_drawdown | 0.8295 |
| cagr | -0.4974 |
| net_avg_win | 46.1290 |
| net_avg_loss | -59.7565 |
| avg_hold_time_bars | 20.5576 |
| exposure | 0.6485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
