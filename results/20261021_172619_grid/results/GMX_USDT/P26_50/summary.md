# EMA Hourly Continuation — GMX/USDT P26_50

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6118 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.5722 |
| sortino_ratio | -1.1432 |
| max_drawdown | 0.7394 |
| cagr | -0.4073 |
| net_avg_win | 49.4622 |
| net_avg_loss | -70.0242 |
| avg_hold_time_bars | 6.3506 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
