# EMA Hourly Continuation — PYTH/USDT P26_50

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.4802 |
| net_win_rate | 0.4546 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -6.8842 |
| sortino_ratio | -2.9777 |
| max_drawdown | 0.9757 |
| cagr | -0.7696 |
| net_avg_win | 20.8975 |
| net_avg_loss | -36.2788 |
| avg_hold_time_bars | 3.4557 |
| exposure | 0.1489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
