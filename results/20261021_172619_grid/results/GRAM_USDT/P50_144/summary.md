# EMA Hourly Continuation — GRAM/USDT P50_144

**Symbol:** GRAM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6925 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9337 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.0480 |
| sortino_ratio | -0.5388 |
| max_drawdown | 0.4887 |
| cagr | -0.2191 |
| net_avg_win | 63.1474 |
| net_avg_loss | -86.4672 |
| avg_hold_time_bars | 16.3599 |
| exposure | 0.2521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
