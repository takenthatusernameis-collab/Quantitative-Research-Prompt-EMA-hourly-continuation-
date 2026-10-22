# EMA Hourly Continuation — CVX/USDT P50_55

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.2462 |
| net_win_rate | 0.3715 |
| gross_profit_factor | 0.7469 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -11.0968 |
| sortino_ratio | -4.5104 |
| max_drawdown | 0.9978 |
| cagr | -0.9130 |
| net_avg_win | 11.0483 |
| net_avg_loss | -26.5281 |
| avg_hold_time_bars | 2.0693 |
| exposure | 0.0747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
