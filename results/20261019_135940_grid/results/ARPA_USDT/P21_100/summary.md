# EMA Hourly Continuation — ARPA/USDT P21_100

**Symbol:** ARPA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.6144 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.9499 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -5.0724 |
| sortino_ratio | -1.9336 |
| max_drawdown | 0.9115 |
| cagr | -0.6062 |
| net_avg_win | 42.1581 |
| net_avg_loss | -58.8102 |
| avg_hold_time_bars | 12.2713 |
| exposure | 0.4115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
