# EMA Hourly Continuation — MOCA/USDT P8_26

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1348 |
| net_profit_factor | 0.4724 |
| net_win_rate | 0.4310 |
| gross_profit_factor | 0.8136 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -10.3738 |
| sortino_ratio | -5.6094 |
| max_drawdown | 0.9984 |
| cagr | -0.9403 |
| net_avg_win | 15.3840 |
| net_avg_loss | -24.6698 |
| avg_hold_time_bars | 4.0319 |
| exposure | 0.2725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
