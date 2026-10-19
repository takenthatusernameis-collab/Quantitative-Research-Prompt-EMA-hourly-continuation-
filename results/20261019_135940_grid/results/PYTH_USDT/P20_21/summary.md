# EMA Hourly Continuation — PYTH/USDT P20_21

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.1617 |
| net_win_rate | 0.3252 |
| gross_profit_factor | 0.6037 |
| gross_win_rate | 0.3733 |
| sharpe_ratio | -16.4423 |
| sortino_ratio | -8.3725 |
| max_drawdown | 1.0000 |
| cagr | -0.9915 |
| net_avg_win | 5.0110 |
| net_avg_loss | -14.9301 |
| avg_hold_time_bars | 1.5414 |
| exposure | 0.0830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
