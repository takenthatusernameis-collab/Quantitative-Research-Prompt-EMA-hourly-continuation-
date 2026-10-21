# EMA Hourly Continuation — VELO/USDT P34_100

**Symbol:** VELO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.9012 |
| net_win_rate | 0.5246 |
| gross_profit_factor | 1.0899 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -0.6301 |
| sortino_ratio | -0.1875 |
| max_drawdown | 0.3200 |
| cagr | -0.0866 |
| net_avg_win | 82.8380 |
| net_avg_loss | -101.4303 |
| avg_hold_time_bars | 12.3911 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
