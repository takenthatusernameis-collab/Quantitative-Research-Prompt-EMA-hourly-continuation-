# EMA Hourly Continuation — UMA/USDT P55_200

**Symbol:** UMA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9495 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -2.9917 |
| sortino_ratio | -0.8728 |
| max_drawdown | 0.6517 |
| cagr | -0.3358 |
| net_avg_win | 51.2521 |
| net_avg_loss | -76.0185 |
| avg_hold_time_bars | 17.7300 |
| exposure | 0.3433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
