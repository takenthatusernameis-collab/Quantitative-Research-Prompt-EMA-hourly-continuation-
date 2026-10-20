# EMA Hourly Continuation — PUFFER/USDT P26_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9999 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -4.5749 |
| sortino_ratio | -1.8936 |
| max_drawdown | 0.8414 |
| cagr | -0.5950 |
| net_avg_win | 40.5109 |
| net_avg_loss | -62.7841 |
| avg_hold_time_bars | 5.0247 |
| exposure | 0.1956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
