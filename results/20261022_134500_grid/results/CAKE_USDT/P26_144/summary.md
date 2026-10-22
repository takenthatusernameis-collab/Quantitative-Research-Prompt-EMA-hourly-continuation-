# EMA Hourly Continuation — CAKE/USDT P26_144

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.5556 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8915 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -3.9691 |
| sortino_ratio | -1.1612 |
| max_drawdown | 0.7895 |
| cagr | -0.4394 |
| net_avg_win | 47.4253 |
| net_avg_loss | -71.2493 |
| avg_hold_time_bars | 23.9685 |
| exposure | 0.4837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
