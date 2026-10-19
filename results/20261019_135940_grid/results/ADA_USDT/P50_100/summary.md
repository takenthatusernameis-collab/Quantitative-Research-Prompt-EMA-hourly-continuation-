# EMA Hourly Continuation — ADA/USDT P50_100

**Symbol:** ADA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.4158 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.7530 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -5.3896 |
| sortino_ratio | -1.8587 |
| max_drawdown | 0.8985 |
| cagr | -0.5957 |
| net_avg_win | 23.5633 |
| net_avg_loss | -47.2511 |
| avg_hold_time_bars | 5.9413 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
