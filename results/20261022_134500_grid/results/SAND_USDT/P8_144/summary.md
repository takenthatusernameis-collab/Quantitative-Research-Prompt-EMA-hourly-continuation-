# EMA Hourly Continuation — SAND/USDT P8_144

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6934 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0318 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -2.0937 |
| sortino_ratio | -0.5568 |
| max_drawdown | 0.5089 |
| cagr | -0.2342 |
| net_avg_win | 61.3574 |
| net_avg_loss | -89.4804 |
| avg_hold_time_bars | 50.2011 |
| exposure | 0.8169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
