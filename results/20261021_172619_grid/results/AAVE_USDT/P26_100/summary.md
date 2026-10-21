# EMA Hourly Continuation — AAVE/USDT P26_100

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7795 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.6282 |
| sortino_ratio | -0.4646 |
| max_drawdown | 0.4591 |
| cagr | -0.1928 |
| net_avg_win | 75.4082 |
| net_avg_loss | -92.4758 |
| avg_hold_time_bars | 17.6291 |
| exposure | 0.3197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
