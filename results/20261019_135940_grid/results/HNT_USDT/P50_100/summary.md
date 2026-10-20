# EMA Hourly Continuation — HNT/USDT P50_100

**Symbol:** HNT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.4919 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.7802 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.3501 |
| sortino_ratio | -1.9859 |
| max_drawdown | 0.9121 |
| cagr | -0.6116 |
| net_avg_win | 28.5114 |
| net_avg_loss | -46.9769 |
| avg_hold_time_bars | 6.3750 |
| exposure | 0.1994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
