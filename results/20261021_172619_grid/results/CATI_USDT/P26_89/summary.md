# EMA Hourly Continuation — CATI/USDT P26_89

**Symbol:** CATI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.7850 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -2.8213 |
| sortino_ratio | -0.8249 |
| max_drawdown | 0.6017 |
| cagr | -0.3171 |
| net_avg_win | 59.4575 |
| net_avg_loss | -76.9796 |
| avg_hold_time_bars | 16.4731 |
| exposure | 0.3188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
