# EMA Hourly Continuation — GMX/USDT P34_50

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5536 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8383 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -3.4014 |
| sortino_ratio | -0.9434 |
| max_drawdown | 0.6676 |
| cagr | -0.3509 |
| net_avg_win | 47.4819 |
| net_avg_loss | -73.4506 |
| avg_hold_time_bars | 5.0240 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
