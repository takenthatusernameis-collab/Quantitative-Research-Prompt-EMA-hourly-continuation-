# EMA Hourly Continuation — DOGE/USDT P21_55

**Symbol:** DOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.7319 |
| sortino_ratio | -0.8394 |
| max_drawdown | 0.6320 |
| cagr | -0.3193 |
| net_avg_win | 58.5844 |
| net_avg_loss | -79.4255 |
| avg_hold_time_bars | 9.2619 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
