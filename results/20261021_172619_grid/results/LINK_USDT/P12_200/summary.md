# EMA Hourly Continuation — LINK/USDT P12_200

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.9217 |
| net_win_rate | 0.5316 |
| gross_profit_factor | 1.1279 |
| gross_win_rate | 0.5316 |
| sharpe_ratio | -0.3853 |
| sortino_ratio | -0.0965 |
| max_drawdown | 0.1757 |
| cagr | -0.0470 |
| net_avg_win | 83.7026 |
| net_avg_loss | -103.0505 |
| avg_hold_time_bars | 51.0100 |
| exposure | 0.6979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
