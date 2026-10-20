# EMA Hourly Continuation — ZETA/USDT P21_55

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.5779 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -6.4284 |
| sortino_ratio | -2.7682 |
| max_drawdown | 0.9658 |
| cagr | -0.7369 |
| net_avg_win | 30.9526 |
| net_avg_loss | -45.0243 |
| avg_hold_time_bars | 5.8385 |
| exposure | 0.2470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
