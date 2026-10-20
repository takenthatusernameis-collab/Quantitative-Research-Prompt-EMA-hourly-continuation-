# EMA Hourly Continuation — AMP/USDT P34_100

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.3650 |
| net_win_rate | 0.3631 |
| gross_profit_factor | 0.6657 |
| gross_win_rate | 0.3806 |
| sharpe_ratio | -10.0574 |
| sortino_ratio | -4.3110 |
| max_drawdown | 0.9957 |
| cagr | -0.8830 |
| net_avg_win | 17.1848 |
| net_avg_loss | -26.8439 |
| avg_hold_time_bars | 7.6968 |
| exposure | 0.3208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
