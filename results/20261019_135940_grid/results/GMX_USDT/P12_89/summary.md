# EMA Hourly Continuation — GMX/USDT P12_89

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.5982 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.9022 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.7404 |
| sortino_ratio | -1.8406 |
| max_drawdown | 0.8904 |
| cagr | -0.5788 |
| net_avg_win | 38.4621 |
| net_avg_loss | -53.6557 |
| avg_hold_time_bars | 15.4549 |
| exposure | 0.5297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
