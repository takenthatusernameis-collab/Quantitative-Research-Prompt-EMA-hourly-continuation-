# EMA Hourly Continuation — DOGS/USDT P12_55

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -2.2824 |
| sortino_ratio | -0.7695 |
| max_drawdown | 0.5476 |
| cagr | -0.2982 |
| net_avg_win | 61.6552 |
| net_avg_loss | -76.9437 |
| avg_hold_time_bars | 13.9917 |
| exposure | 0.3563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
