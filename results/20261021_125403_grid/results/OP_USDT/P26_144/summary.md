# EMA Hourly Continuation — OP/USDT P26_144

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7497 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9116 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -1.7055 |
| sortino_ratio | -0.4433 |
| max_drawdown | 0.4248 |
| cagr | -0.1846 |
| net_avg_win | 75.5537 |
| net_avg_loss | -91.5606 |
| avg_hold_time_bars | 33.4281 |
| exposure | 0.5075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
