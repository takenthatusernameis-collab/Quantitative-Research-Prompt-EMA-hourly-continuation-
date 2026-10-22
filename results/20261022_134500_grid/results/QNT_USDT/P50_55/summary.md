# EMA Hourly Continuation — QNT/USDT P50_55

**Symbol:** QNT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.1478 |
| net_win_rate | 0.3079 |
| gross_profit_factor | 0.6123 |
| gross_win_rate | 0.3799 |
| sharpe_ratio | -14.8422 |
| sortino_ratio | -6.7715 |
| max_drawdown | 0.9999 |
| cagr | -0.9760 |
| net_avg_win | 6.1520 |
| net_avg_loss | -18.5079 |
| avg_hold_time_bars | 1.8362 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
