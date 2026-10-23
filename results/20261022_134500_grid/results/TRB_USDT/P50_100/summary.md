# EMA Hourly Continuation — TRB/USDT P50_100

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.4322 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.7581 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -6.7292 |
| sortino_ratio | -2.4408 |
| max_drawdown | 0.9505 |
| cagr | -0.6956 |
| net_avg_win | 26.2113 |
| net_avg_loss | -43.3588 |
| avg_hold_time_bars | 6.3640 |
| exposure | 0.1906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
