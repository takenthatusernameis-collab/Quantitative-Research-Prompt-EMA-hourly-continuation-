# EMA Hourly Continuation — ETN/USDT P8_200

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.5153 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7062 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -5.6027 |
| sortino_ratio | -2.0310 |
| max_drawdown | 0.8762 |
| cagr | -0.6263 |
| net_avg_win | 39.6916 |
| net_avg_loss | -54.1261 |
| avg_hold_time_bars | 21.7143 |
| exposure | 0.6688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
