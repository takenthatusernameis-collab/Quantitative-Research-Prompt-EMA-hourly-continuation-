# EMA Hourly Continuation — API3/USDT P50_100

**Symbol:** API3/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7654 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0136 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.6376 |
| sortino_ratio | -0.4598 |
| max_drawdown | 0.4570 |
| cagr | -0.1906 |
| net_avg_win | 69.6538 |
| net_avg_loss | -92.4347 |
| avg_hold_time_bars | 10.2742 |
| exposure | 0.1789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
