# EMA Hourly Continuation — MANA/USDT P100_144

**Symbol:** MANA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.4244 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -6.3650 |
| sortino_ratio | -2.1186 |
| max_drawdown | 0.9361 |
| cagr | -0.6599 |
| net_avg_win | 27.4143 |
| net_avg_loss | -52.6455 |
| avg_hold_time_bars | 3.4347 |
| exposure | 0.0873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
