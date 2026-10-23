# EMA Hourly Continuation — CFG/USDT P20_200

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8700 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -2.3476 |
| sortino_ratio | -0.5856 |
| max_drawdown | 0.5358 |
| cagr | -0.2443 |
| net_avg_win | 61.6089 |
| net_avg_loss | -82.4970 |
| avg_hold_time_bars | 48.5094 |
| exposure | 0.7012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
