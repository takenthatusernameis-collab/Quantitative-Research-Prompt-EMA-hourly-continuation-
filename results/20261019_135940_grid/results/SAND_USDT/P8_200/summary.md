# EMA Hourly Continuation — SAND/USDT P8_200

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0261 |
| sortino_ratio | -0.4758 |
| max_drawdown | 0.4628 |
| cagr | -0.2031 |
| net_avg_win | 57.2851 |
| net_avg_loss | -86.2766 |
| avg_hold_time_bars | 66.5571 |
| exposure | 0.8471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
