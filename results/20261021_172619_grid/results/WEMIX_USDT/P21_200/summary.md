# EMA Hourly Continuation — WEMIX/USDT P21_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.5365 |
| net_win_rate | 0.3937 |
| gross_profit_factor | 0.6603 |
| gross_win_rate | 0.3937 |
| sharpe_ratio | -3.6262 |
| sortino_ratio | -0.9123 |
| max_drawdown | 0.6563 |
| cagr | -0.3452 |
| net_avg_win | 60.1410 |
| net_avg_loss | -72.8063 |
| avg_hold_time_bars | 44.9969 |
| exposure | 0.6545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
