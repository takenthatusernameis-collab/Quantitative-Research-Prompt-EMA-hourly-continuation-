# EMA Hourly Continuation — LINK/USDT P50_144

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8309 |
| net_win_rate | 0.5217 |
| gross_profit_factor | 1.0900 |
| gross_win_rate | 0.5217 |
| sharpe_ratio | -1.0322 |
| sortino_ratio | -0.2667 |
| max_drawdown | 0.3227 |
| cagr | -0.1161 |
| net_avg_win | 77.9096 |
| net_avg_loss | -102.2930 |
| avg_hold_time_bars | 16.7857 |
| exposure | 0.2457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
