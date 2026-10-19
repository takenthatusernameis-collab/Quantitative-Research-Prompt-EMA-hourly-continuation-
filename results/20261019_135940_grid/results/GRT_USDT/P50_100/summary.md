# EMA Hourly Continuation — GRT/USDT P50_100

**Symbol:** GRT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5415 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9152 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -4.6218 |
| sortino_ratio | -1.6383 |
| max_drawdown | 0.8683 |
| cagr | -0.5460 |
| net_avg_win | 33.7705 |
| net_avg_loss | -56.5600 |
| avg_hold_time_bars | 5.5732 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
