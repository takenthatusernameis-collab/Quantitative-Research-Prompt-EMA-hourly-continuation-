# EMA Hourly Continuation — ENJ/USDT P34_50

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.4282 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -8.6124 |
| sortino_ratio | -3.7487 |
| max_drawdown | 0.9918 |
| cagr | -0.8512 |
| net_avg_win | 17.4723 |
| net_avg_loss | -33.0327 |
| avg_hold_time_bars | 2.6695 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
