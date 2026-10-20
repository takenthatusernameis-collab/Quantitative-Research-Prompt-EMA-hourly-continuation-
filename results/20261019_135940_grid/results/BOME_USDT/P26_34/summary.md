# EMA Hourly Continuation — BOME/USDT P26_34

**Symbol:** BOME/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.3377 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7543 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -9.8222 |
| sortino_ratio | -4.4365 |
| max_drawdown | 0.9969 |
| cagr | -0.8961 |
| net_avg_win | 11.8171 |
| net_avg_loss | -25.7221 |
| avg_hold_time_bars | 2.0857 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
