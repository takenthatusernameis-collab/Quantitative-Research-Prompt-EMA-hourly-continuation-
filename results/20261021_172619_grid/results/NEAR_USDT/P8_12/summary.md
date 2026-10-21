# EMA Hourly Continuation — NEAR/USDT P8_12

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.8675 |
| net_win_rate | 0.5380 |
| gross_profit_factor | 1.1611 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -0.5940 |
| sortino_ratio | -0.1166 |
| max_drawdown | 0.1979 |
| cagr | -0.0533 |
| net_avg_win | 84.8843 |
| net_avg_loss | -113.9715 |
| avg_hold_time_bars | 4.3478 |
| exposure | 0.0364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
