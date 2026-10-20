# EMA Hourly Continuation — DOGS/USDT P21_89

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6787 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 0.9919 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -3.0756 |
| sortino_ratio | -1.1971 |
| max_drawdown | 0.7031 |
| cagr | -0.4294 |
| net_avg_win | 45.7060 |
| net_avg_loss | -68.3958 |
| avg_hold_time_bars | 10.7776 |
| exposure | 0.3676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
