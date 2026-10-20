# EMA Hourly Continuation — WIN/USDT P89_200

**Symbol:** WIN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.3062 |
| net_win_rate | 0.3838 |
| gross_profit_factor | 0.6469 |
| gross_win_rate | 0.4027 |
| sharpe_ratio | -5.9597 |
| sortino_ratio | -1.6339 |
| max_drawdown | 0.8691 |
| cagr | -0.5522 |
| net_avg_win | 26.9431 |
| net_avg_loss | -54.8080 |
| avg_hold_time_bars | 12.6189 |
| exposure | 0.2122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
