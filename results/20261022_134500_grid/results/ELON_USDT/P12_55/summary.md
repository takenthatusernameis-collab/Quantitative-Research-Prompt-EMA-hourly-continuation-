# EMA Hourly Continuation — ELON/USDT P12_55

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1044 |
| net_profit_factor | 0.4655 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.7768 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -7.3413 |
| sortino_ratio | -3.3552 |
| max_drawdown | 0.9824 |
| cagr | -0.7993 |
| net_avg_win | 18.6000 |
| net_avg_loss | -31.4705 |
| avg_hold_time_bars | 7.4128 |
| exposure | 0.3518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
