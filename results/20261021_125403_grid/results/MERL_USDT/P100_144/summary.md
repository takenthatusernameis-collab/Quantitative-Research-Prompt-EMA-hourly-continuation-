# EMA Hourly Continuation — MERL/USDT P100_144

**Symbol:** MERL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.7632 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9630 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.3591 |
| sortino_ratio | -0.3021 |
| max_drawdown | 0.3237 |
| cagr | -0.1305 |
| net_avg_win | 80.7067 |
| net_avg_loss | -101.4507 |
| avg_hold_time_bars | 6.4274 |
| exposure | 0.0706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
