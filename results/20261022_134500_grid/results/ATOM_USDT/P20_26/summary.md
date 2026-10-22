# EMA Hourly Continuation — ATOM/USDT P20_26

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1130 |
| net_profit_factor | 0.1580 |
| net_win_rate | 0.3451 |
| gross_profit_factor | 0.6222 |
| gross_win_rate | 0.4044 |
| sharpe_ratio | -14.8979 |
| sortino_ratio | -7.3796 |
| max_drawdown | 1.0000 |
| cagr | -0.9813 |
| net_avg_win | 4.8119 |
| net_avg_loss | -16.0489 |
| avg_hold_time_bars | 1.8832 |
| exposure | 0.0967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
