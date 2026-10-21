# EMA Hourly Continuation — TFUEL/USDT P12_21

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5014 |
| net_win_rate | 0.4018 |
| gross_profit_factor | 0.7695 |
| gross_win_rate | 0.4018 |
| sharpe_ratio | -5.5048 |
| sortino_ratio | -1.6745 |
| max_drawdown | 0.8631 |
| cagr | -0.5399 |
| net_avg_win | 47.4575 |
| net_avg_loss | -63.5664 |
| avg_hold_time_bars | 4.8675 |
| exposure | 0.0998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
