# EMA Hourly Continuation — CAKE/USDT P21_144

**Symbol:** CAKE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6022 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -3.5266 |
| sortino_ratio | -1.0689 |
| max_drawdown | 0.7664 |
| cagr | -0.4093 |
| net_avg_win | 49.5565 |
| net_avg_loss | -73.4461 |
| avg_hold_time_bars | 24.1747 |
| exposure | 0.5220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
