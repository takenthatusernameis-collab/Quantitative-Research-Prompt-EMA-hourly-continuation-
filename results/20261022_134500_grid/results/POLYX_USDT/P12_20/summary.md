# EMA Hourly Continuation — POLYX/USDT P12_20

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.3341 |
| net_win_rate | 0.4170 |
| gross_profit_factor | 0.8081 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -11.7834 |
| sortino_ratio | -6.2170 |
| max_drawdown | 0.9996 |
| cagr | -0.9550 |
| net_avg_win | 8.8767 |
| net_avg_loss | -19.0015 |
| avg_hold_time_bars | 2.7963 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
