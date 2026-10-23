# EMA Hourly Continuation — SATS/USDT P26_34

**Symbol:** SATS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.3624 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.8978 |
| gross_win_rate | 0.4369 |
| sharpe_ratio | -8.5431 |
| sortino_ratio | -3.4399 |
| max_drawdown | 0.9878 |
| cagr | -0.8232 |
| net_avg_win | 16.6500 |
| net_avg_loss | -32.8763 |
| avg_hold_time_bars | 2.6126 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
