# EMA Hourly Continuation — POLYX/USDT P50_144

**Symbol:** POLYX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7207 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.1066 |
| sortino_ratio | -0.5772 |
| max_drawdown | 0.5029 |
| cagr | -0.2331 |
| net_avg_win | 70.9064 |
| net_avg_loss | -90.7048 |
| avg_hold_time_bars | 16.8130 |
| exposure | 0.2820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
