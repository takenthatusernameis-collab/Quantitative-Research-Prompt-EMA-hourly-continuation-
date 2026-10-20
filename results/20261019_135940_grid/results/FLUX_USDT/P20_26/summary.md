# EMA Hourly Continuation — FLUX/USDT P20_26

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1198 |
| net_profit_factor | 0.2546 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 0.7720 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -13.8437 |
| sortino_ratio | -6.9360 |
| max_drawdown | 0.9999 |
| cagr | -0.9743 |
| net_avg_win | 7.6397 |
| net_avg_loss | -17.8614 |
| avg_hold_time_bars | 1.8589 |
| exposure | 0.1012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
