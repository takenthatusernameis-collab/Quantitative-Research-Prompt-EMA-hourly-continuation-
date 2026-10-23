# EMA Hourly Continuation — GMX/USDT P55_200

**Symbol:** GMX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.6491 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.9193 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -3.2490 |
| sortino_ratio | -0.9512 |
| max_drawdown | 0.7154 |
| cagr | -0.3655 |
| net_avg_win | 63.2895 |
| net_avg_loss | -82.5707 |
| avg_hold_time_bars | 17.1498 |
| exposure | 0.3383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
