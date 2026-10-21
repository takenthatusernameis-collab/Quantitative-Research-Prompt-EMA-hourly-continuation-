# EMA Hourly Continuation — AGLD/USDT P20_34

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6798 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -3.0333 |
| sortino_ratio | -1.0325 |
| max_drawdown | 0.7186 |
| cagr | -0.3755 |
| net_avg_win | 53.6644 |
| net_avg_loss | -74.5962 |
| avg_hold_time_bars | 5.3534 |
| exposure | 0.1371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
