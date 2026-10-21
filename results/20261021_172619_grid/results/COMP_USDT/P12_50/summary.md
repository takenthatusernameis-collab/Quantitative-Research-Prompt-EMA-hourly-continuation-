# EMA Hourly Continuation — COMP/USDT P12_50

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.8603 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -3.4671 |
| sortino_ratio | -1.3191 |
| max_drawdown | 0.7919 |
| cagr | -0.4538 |
| net_avg_win | 39.5718 |
| net_avg_loss | -57.1034 |
| avg_hold_time_bars | 10.8491 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
