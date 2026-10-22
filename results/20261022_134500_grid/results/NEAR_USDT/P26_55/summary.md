# EMA Hourly Continuation — NEAR/USDT P26_55

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 937 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -6.9686 |
| sortino_ratio | -2.9876 |
| max_drawdown | 0.9764 |
| cagr | -0.7742 |
| net_avg_win | 23.3816 |
| net_avg_loss | -38.7172 |
| avg_hold_time_bars | 3.9947 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
