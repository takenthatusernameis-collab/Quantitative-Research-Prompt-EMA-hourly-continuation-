# EMA Hourly Continuation — QNT/USDT P50_55

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 120 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.5362 |
| sortino_ratio | -0.2420 |
| max_drawdown | 0.2611 |
| cagr | -0.1045 |
| net_avg_win | 72.1712 |
| net_avg_loss | -109.5043 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
