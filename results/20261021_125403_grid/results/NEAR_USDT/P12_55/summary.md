# EMA Hourly Continuation — NEAR/USDT P12_55

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7824 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -1.8589 |
| sortino_ratio | -0.6404 |
| max_drawdown | 0.5369 |
| cagr | -0.2563 |
| net_avg_win | 66.1910 |
| net_avg_loss | -81.4533 |
| avg_hold_time_bars | 13.4079 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
