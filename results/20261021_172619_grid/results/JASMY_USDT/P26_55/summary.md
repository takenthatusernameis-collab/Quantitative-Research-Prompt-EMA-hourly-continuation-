# EMA Hourly Continuation — JASMY/USDT P26_55

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7210 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.8926 |
| sortino_ratio | -0.5224 |
| max_drawdown | 0.4593 |
| cagr | -0.2134 |
| net_avg_win | 64.2790 |
| net_avg_loss | -85.3957 |
| avg_hold_time_bars | 6.6237 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
