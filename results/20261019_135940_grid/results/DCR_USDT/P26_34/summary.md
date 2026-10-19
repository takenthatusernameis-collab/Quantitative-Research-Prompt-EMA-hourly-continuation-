# EMA Hourly Continuation — DCR/USDT P26_34

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1086 |
| net_profit_factor | 0.2682 |
| net_win_rate | 0.3610 |
| gross_profit_factor | 0.7276 |
| gross_win_rate | 0.4070 |
| sharpe_ratio | -13.1285 |
| sortino_ratio | -6.2537 |
| max_drawdown | 0.9997 |
| cagr | -0.9615 |
| net_avg_win | 9.3463 |
| net_avg_loss | -19.6845 |
| avg_hold_time_bars | 2.6519 |
| exposure | 0.1303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
