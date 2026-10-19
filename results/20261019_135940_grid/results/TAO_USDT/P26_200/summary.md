# EMA Hourly Continuation — TAO/USDT P26_200

**Symbol:** TAO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -1.9710 |
| sortino_ratio | -0.5729 |
| max_drawdown | 0.5110 |
| cagr | -0.2348 |
| net_avg_win | 66.9068 |
| net_avg_loss | -86.9586 |
| avg_hold_time_bars | 28.2315 |
| exposure | 0.5377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
