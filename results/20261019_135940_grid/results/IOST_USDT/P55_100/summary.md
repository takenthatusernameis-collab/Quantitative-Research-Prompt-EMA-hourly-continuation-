# EMA Hourly Continuation — IOST/USDT P55_100

**Symbol:** IOST/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.5307 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -4.9958 |
| sortino_ratio | -1.7406 |
| max_drawdown | 0.8867 |
| cagr | -0.5749 |
| net_avg_win | 33.7416 |
| net_avg_loss | -59.7474 |
| avg_hold_time_bars | 6.0082 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
