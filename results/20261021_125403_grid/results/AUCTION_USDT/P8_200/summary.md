# EMA Hourly Continuation — AUCTION/USDT P8_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7661 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9469 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.4960 |
| sortino_ratio | -0.3742 |
| max_drawdown | 0.3798 |
| cagr | -0.1594 |
| net_avg_win | 77.4279 |
| net_avg_loss | -94.7558 |
| avg_hold_time_bars | 56.9935 |
| exposure | 0.7996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
