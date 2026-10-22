# EMA Hourly Continuation — ONDO/USDT P8_21

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1664 |
| net_profit_factor | 0.3948 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.7717 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -10.6046 |
| sortino_ratio | -6.0859 |
| max_drawdown | 0.9995 |
| cagr | -0.9530 |
| net_avg_win | 8.7998 |
| net_avg_loss | -17.8939 |
| avg_hold_time_bars | 2.8684 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
