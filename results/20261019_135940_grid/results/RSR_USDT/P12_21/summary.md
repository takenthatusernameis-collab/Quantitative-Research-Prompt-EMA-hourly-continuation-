# EMA Hourly Continuation — RSR/USDT P12_21

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1436 |
| net_profit_factor | 0.4459 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.9769 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -10.6075 |
| sortino_ratio | -5.6630 |
| max_drawdown | 0.9993 |
| cagr | -0.9438 |
| net_avg_win | 12.5053 |
| net_avg_loss | -22.7411 |
| avg_hold_time_bars | 2.3607 |
| exposure | 0.1541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
