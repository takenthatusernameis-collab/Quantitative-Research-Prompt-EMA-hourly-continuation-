# EMA Hourly Continuation — OSMO/USDT P26_89

**Symbol:** OSMO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.9650 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -4.9644 |
| sortino_ratio | -1.8248 |
| max_drawdown | 0.8901 |
| cagr | -0.5814 |
| net_avg_win | 41.9726 |
| net_avg_loss | -58.3024 |
| avg_hold_time_bars | 10.6246 |
| exposure | 0.3294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
