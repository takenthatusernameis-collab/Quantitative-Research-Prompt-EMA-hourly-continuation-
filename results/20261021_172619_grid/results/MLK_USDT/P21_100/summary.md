# EMA Hourly Continuation — MLK/USDT P21_100

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.4807 |
| net_win_rate | 0.3642 |
| gross_profit_factor | 0.6429 |
| gross_win_rate | 0.3662 |
| sharpe_ratio | -5.6712 |
| sortino_ratio | -1.7797 |
| max_drawdown | 0.8786 |
| cagr | -0.5630 |
| net_avg_win | 44.8020 |
| net_avg_loss | -53.3866 |
| avg_hold_time_bars | 14.9396 |
| exposure | 0.3360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
