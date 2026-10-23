# EMA Hourly Continuation — PIXEL/USDT P8_20

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1642 |
| net_profit_factor | 0.5223 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -9.4864 |
| sortino_ratio | -5.4034 |
| max_drawdown | 0.9987 |
| cagr | -0.9290 |
| net_avg_win | 14.7385 |
| net_avg_loss | -23.2059 |
| avg_hold_time_bars | 3.1577 |
| exposure | 0.2346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
