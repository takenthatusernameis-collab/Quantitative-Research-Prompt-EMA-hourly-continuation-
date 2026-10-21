# EMA Hourly Continuation — ZIL/USDT P26_55

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7074 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -2.2728 |
| sortino_ratio | -0.6902 |
| max_drawdown | 0.5660 |
| cagr | -0.2704 |
| net_avg_win | 59.0346 |
| net_avg_loss | -84.1997 |
| avg_hold_time_bars | 6.6749 |
| exposure | 0.1353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
