# EMA Hourly Continuation — DEEP/USDT P20_26

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 144 |
| net_profit_factor | 1.2015 |
| net_win_rate | 0.6250 |
| gross_profit_factor | 1.6411 |
| gross_win_rate | 0.6250 |
| sharpe_ratio | 0.8269 |
| sortino_ratio | 0.1649 |
| max_drawdown | 0.0841 |
| cagr | 0.0679 |
| net_avg_win | 93.7480 |
| net_avg_loss | -130.0391 |
| avg_hold_time_bars | 4.5556 |
| exposure | 0.0371 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
