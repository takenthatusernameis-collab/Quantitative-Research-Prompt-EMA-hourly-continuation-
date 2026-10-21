# EMA Hourly Continuation — DEGEN/USDT P50_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8794 |
| net_win_rate | 0.5214 |
| gross_profit_factor | 1.0827 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -0.7606 |
| sortino_ratio | -0.2119 |
| max_drawdown | 0.2642 |
| cagr | -0.0956 |
| net_avg_win | 83.3292 |
| net_avg_loss | -103.2226 |
| avg_hold_time_bars | 9.9198 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
