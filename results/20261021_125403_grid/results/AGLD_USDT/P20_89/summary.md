# EMA Hourly Continuation — AGLD/USDT P20_89

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7400 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -2.6249 |
| sortino_ratio | -0.8789 |
| max_drawdown | 0.7088 |
| cagr | -0.3327 |
| net_avg_win | 69.4539 |
| net_avg_loss | -83.6464 |
| avg_hold_time_bars | 16.0054 |
| exposure | 0.4027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
