# EMA Hourly Continuation — DEEP/USDT P89_100

**Symbol:** DEEP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 82 |
| net_profit_factor | 0.8854 |
| net_win_rate | 0.5366 |
| gross_profit_factor | 1.1504 |
| gross_win_rate | 0.5366 |
| sharpe_ratio | -0.3645 |
| sortino_ratio | -0.0533 |
| max_drawdown | 0.1183 |
| cagr | -0.0250 |
| net_avg_win | 87.2969 |
| net_avg_loss | -114.1673 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
