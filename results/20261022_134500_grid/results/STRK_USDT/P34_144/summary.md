# EMA Hourly Continuation — STRK/USDT P34_144

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.6590 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.7017 |
| sortino_ratio | -0.8392 |
| max_drawdown | 0.6723 |
| cagr | -0.3248 |
| net_avg_win | 52.6812 |
| net_avg_loss | -73.5506 |
| avg_hold_time_bars | 17.5208 |
| exposure | 0.3823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
