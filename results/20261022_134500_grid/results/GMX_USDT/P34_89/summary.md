# EMA Hourly Continuation — GMX/USDT P34_89

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5471 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -5.2955 |
| sortino_ratio | -1.9559 |
| max_drawdown | 0.9056 |
| cagr | -0.6044 |
| net_avg_win | 35.4035 |
| net_avg_loss | -53.1474 |
| avg_hold_time_bars | 8.1435 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
