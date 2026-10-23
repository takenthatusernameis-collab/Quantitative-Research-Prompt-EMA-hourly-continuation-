# EMA Hourly Continuation — UMA/USDT P8_55

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.5776 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -5.6645 |
| sortino_ratio | -2.5694 |
| max_drawdown | 0.9577 |
| cagr | -0.7102 |
| net_avg_win | 26.3931 |
| net_avg_loss | -41.2752 |
| avg_hold_time_bars | 10.0297 |
| exposure | 0.4755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
