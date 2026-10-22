# EMA Hourly Continuation — PENDLE/USDT P8_26

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1528 |
| net_profit_factor | 0.4959 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -8.5871 |
| sortino_ratio | -4.7198 |
| max_drawdown | 0.9970 |
| cagr | -0.8998 |
| net_avg_win | 13.9678 |
| net_avg_loss | -23.9400 |
| avg_hold_time_bars | 3.9404 |
| exposure | 0.2737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
