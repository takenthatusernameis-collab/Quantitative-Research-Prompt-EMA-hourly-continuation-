# EMA Hourly Continuation — NEO/USDT P50_200

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6181 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -3.0142 |
| sortino_ratio | -0.8633 |
| max_drawdown | 0.6474 |
| cagr | -0.3369 |
| net_avg_win | 52.0886 |
| net_avg_loss | -78.7562 |
| avg_hold_time_bars | 20.9952 |
| exposure | 0.3951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
