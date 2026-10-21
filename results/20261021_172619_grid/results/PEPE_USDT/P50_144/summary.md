# EMA Hourly Continuation — PEPE/USDT P50_144

**Symbol:** PEPE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7913 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9686 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.2718 |
| sortino_ratio | -0.3181 |
| max_drawdown | 0.3298 |
| cagr | -0.1367 |
| net_avg_win | 77.5322 |
| net_avg_loss | -95.4463 |
| avg_hold_time_bars | 20.6667 |
| exposure | 0.2875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
