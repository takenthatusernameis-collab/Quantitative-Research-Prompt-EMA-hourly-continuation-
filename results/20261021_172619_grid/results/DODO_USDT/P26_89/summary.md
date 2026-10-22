# EMA Hourly Continuation — DODO/USDT P26_89

**Symbol:** DODO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7409 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.5325 |
| sortino_ratio | -0.8066 |
| max_drawdown | 0.6636 |
| cagr | -0.3096 |
| net_avg_win | 72.9752 |
| net_avg_loss | -88.7892 |
| avg_hold_time_bars | 13.0896 |
| exposure | 0.2973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
