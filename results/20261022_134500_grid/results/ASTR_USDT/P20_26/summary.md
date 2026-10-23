# EMA Hourly Continuation — ASTR/USDT P20_26

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.2412 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.7943 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -12.6029 |
| sortino_ratio | -5.9902 |
| max_drawdown | 0.9996 |
| cagr | -0.9569 |
| net_avg_win | 7.4052 |
| net_avg_loss | -20.2665 |
| avg_hold_time_bars | 2.6830 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
