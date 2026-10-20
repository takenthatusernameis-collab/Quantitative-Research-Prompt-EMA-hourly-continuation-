# EMA Hourly Continuation — COTI/USDT P55_200

**Symbol:** COTI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8973 |
| net_win_rate | 0.5591 |
| gross_profit_factor | 1.2855 |
| gross_win_rate | 0.5643 |
| sharpe_ratio | -0.5961 |
| sortino_ratio | -0.1646 |
| max_drawdown | 0.2334 |
| cagr | -0.0804 |
| net_avg_win | 77.8555 |
| net_avg_loss | -110.0106 |
| avg_hold_time_bars | 22.3517 |
| exposure | 0.3871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
