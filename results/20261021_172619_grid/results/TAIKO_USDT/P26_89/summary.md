# EMA Hourly Continuation — TAIKO/USDT P26_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8040 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.4793 |
| sortino_ratio | -0.4604 |
| max_drawdown | 0.4243 |
| cagr | -0.1914 |
| net_avg_win | 71.3279 |
| net_avg_loss | -93.6442 |
| avg_hold_time_bars | 13.7545 |
| exposure | 0.2934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
