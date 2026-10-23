# EMA Hourly Continuation — EDU/USDT P34_55

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.4008 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.7262 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -8.1678 |
| sortino_ratio | -3.5105 |
| max_drawdown | 0.9868 |
| cagr | -0.8167 |
| net_avg_win | 17.1331 |
| net_avg_loss | -30.6476 |
| avg_hold_time_bars | 3.6171 |
| exposure | 0.1509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
