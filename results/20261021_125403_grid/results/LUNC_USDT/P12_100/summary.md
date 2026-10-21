# EMA Hourly Continuation — LUNC/USDT P12_100

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8226 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -3.1083 |
| sortino_ratio | -1.0231 |
| max_drawdown | 0.7008 |
| cagr | -0.3756 |
| net_avg_win | 50.7131 |
| net_avg_loss | -66.3009 |
| avg_hold_time_bars | 19.9274 |
| exposure | 0.4864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
