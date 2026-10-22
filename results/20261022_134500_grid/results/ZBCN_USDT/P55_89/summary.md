# EMA Hourly Continuation — ZBCN/USDT P55_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4543 |
| net_win_rate | 0.4307 |
| gross_profit_factor | 0.7932 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -6.5496 |
| sortino_ratio | -2.5397 |
| max_drawdown | 0.9567 |
| cagr | -0.7120 |
| net_avg_win | 24.8112 |
| net_avg_loss | -41.3140 |
| avg_hold_time_bars | 2.9071 |
| exposure | 0.0999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
