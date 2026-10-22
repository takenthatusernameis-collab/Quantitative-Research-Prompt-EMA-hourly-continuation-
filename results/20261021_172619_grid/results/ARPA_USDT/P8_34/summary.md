# EMA Hourly Continuation — ARPA/USDT P8_34

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -4.5762 |
| sortino_ratio | -1.9475 |
| max_drawdown | 0.8978 |
| cagr | -0.5906 |
| net_avg_win | 40.9859 |
| net_avg_loss | -54.5061 |
| avg_hold_time_bars | 7.6282 |
| exposure | 0.3082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
