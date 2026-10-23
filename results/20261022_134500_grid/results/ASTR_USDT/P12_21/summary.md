# EMA Hourly Continuation — ASTR/USDT P12_21

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.3345 |
| net_win_rate | 0.4241 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -11.7643 |
| sortino_ratio | -6.0926 |
| max_drawdown | 0.9996 |
| cagr | -0.9562 |
| net_avg_win | 8.9084 |
| net_avg_loss | -19.6091 |
| avg_hold_time_bars | 3.0699 |
| exposure | 0.1848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
