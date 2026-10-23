# EMA Hourly Continuation — OGN/USDT P26_200

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8411 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -3.5398 |
| sortino_ratio | -1.0248 |
| max_drawdown | 0.7254 |
| cagr | -0.3842 |
| net_avg_win | 50.3944 |
| net_avg_loss | -70.2573 |
| avg_hold_time_bars | 29.7906 |
| exposure | 0.5729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
