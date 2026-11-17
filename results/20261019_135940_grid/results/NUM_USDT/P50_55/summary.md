# EMA Hourly Continuation — NUM/USDT P50_55

**Symbol:** NUM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.1949 |
| net_win_rate | 0.2790 |
| gross_profit_factor | 0.6880 |
| gross_win_rate | 0.3346 |
| sharpe_ratio | -13.5462 |
| sortino_ratio | -5.6640 |
| max_drawdown | 0.9995 |
| cagr | -0.9523 |
| net_avg_win | 10.7081 |
| net_avg_loss | -21.2590 |
| avg_hold_time_bars | 3.8790 |
| exposure | 0.1428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
