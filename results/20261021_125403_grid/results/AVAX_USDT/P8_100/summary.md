# EMA Hourly Continuation — AVAX/USDT P8_100

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.7850 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -1.9156 |
| sortino_ratio | -0.6013 |
| max_drawdown | 0.5335 |
| cagr | -0.2428 |
| net_avg_win | 78.1009 |
| net_avg_loss | -93.5230 |
| avg_hold_time_bars | 28.3814 |
| exposure | 0.6257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
