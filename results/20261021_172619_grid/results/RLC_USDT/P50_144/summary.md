# EMA Hourly Continuation — RLC/USDT P50_144

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0111 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.4299 |
| sortino_ratio | -0.3947 |
| max_drawdown | 0.4047 |
| cagr | -0.1670 |
| net_avg_win | 73.7207 |
| net_avg_loss | -94.9259 |
| avg_hold_time_bars | 17.0162 |
| exposure | 0.2870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
