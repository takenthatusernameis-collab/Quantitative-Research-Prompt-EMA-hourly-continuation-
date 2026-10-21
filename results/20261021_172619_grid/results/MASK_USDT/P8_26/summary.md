# EMA Hourly Continuation — MASK/USDT P8_26

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -3.6256 |
| sortino_ratio | -1.4104 |
| max_drawdown | 0.8060 |
| cagr | -0.4778 |
| net_avg_win | 41.7499 |
| net_avg_loss | -62.0873 |
| avg_hold_time_bars | 7.9324 |
| exposure | 0.2668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
