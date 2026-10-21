# EMA Hourly Continuation — KMNO/USDT P26_89

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9757 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.5823 |
| sortino_ratio | -0.4602 |
| max_drawdown | 0.4511 |
| cagr | -0.1924 |
| net_avg_win | 72.1990 |
| net_avg_loss | -90.7155 |
| avg_hold_time_bars | 15.3922 |
| exposure | 0.2899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
