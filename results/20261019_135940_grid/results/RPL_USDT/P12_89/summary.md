# EMA Hourly Continuation — RPL/USDT P12_89

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6524 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9314 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.4145 |
| sortino_ratio | -1.2389 |
| max_drawdown | 0.7762 |
| cagr | -0.4440 |
| net_avg_win | 45.7455 |
| net_avg_loss | -63.5037 |
| avg_hold_time_bars | 18.5532 |
| exposure | 0.5600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
