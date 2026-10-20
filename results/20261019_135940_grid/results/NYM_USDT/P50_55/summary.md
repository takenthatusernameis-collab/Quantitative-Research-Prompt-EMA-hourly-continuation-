# EMA Hourly Continuation — NYM/USDT P50_55

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.0572 |
| net_win_rate | 0.1902 |
| gross_profit_factor | 0.3980 |
| gross_win_rate | 0.2797 |
| sharpe_ratio | -16.4062 |
| sortino_ratio | -7.1487 |
| max_drawdown | 1.0000 |
| cagr | -0.9834 |
| net_avg_win | 4.4593 |
| net_avg_loss | -18.3180 |
| avg_hold_time_bars | 2.8587 |
| exposure | 0.0929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
