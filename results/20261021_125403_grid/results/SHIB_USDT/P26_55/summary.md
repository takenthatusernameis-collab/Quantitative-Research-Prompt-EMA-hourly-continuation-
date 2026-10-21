# EMA Hourly Continuation — SHIB/USDT P26_55

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7184 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -2.1632 |
| sortino_ratio | -0.6086 |
| max_drawdown | 0.5457 |
| cagr | -0.2429 |
| net_avg_win | 66.8271 |
| net_avg_loss | -93.5032 |
| avg_hold_time_bars | 7.0444 |
| exposure | 0.1226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
