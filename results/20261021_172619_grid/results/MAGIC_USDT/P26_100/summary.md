# EMA Hourly Continuation — MAGIC/USDT P26_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.0379 |
| sortino_ratio | -0.6307 |
| max_drawdown | 0.5301 |
| cagr | -0.2529 |
| net_avg_win | 74.9632 |
| net_avg_loss | -92.7694 |
| avg_hold_time_bars | 18.2106 |
| exposure | 0.3890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
