# EMA Hourly Continuation — STRAX/USDT P8_144

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.5963 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -5.3773 |
| sortino_ratio | -2.0312 |
| max_drawdown | 0.9147 |
| cagr | -0.6258 |
| net_avg_win | 42.4495 |
| net_avg_loss | -55.4894 |
| avg_hold_time_bars | 19.6777 |
| exposure | 0.6532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
