# EMA Hourly Continuation — DODO/USDT P34_89

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7574 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.0969 |
| sortino_ratio | -0.6510 |
| max_drawdown | 0.5589 |
| cagr | -0.2583 |
| net_avg_win | 70.9114 |
| net_avg_loss | -90.8998 |
| avg_hold_time_bars | 9.7040 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
