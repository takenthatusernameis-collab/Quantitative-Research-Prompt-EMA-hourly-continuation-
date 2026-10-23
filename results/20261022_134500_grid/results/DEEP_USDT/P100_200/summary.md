# EMA Hourly Continuation — DEEP/USDT P100_200

**Symbol:** DEEP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.6039 |
| sortino_ratio | -0.7024 |
| max_drawdown | 0.5171 |
| cagr | -0.2900 |
| net_avg_win | 61.8192 |
| net_avg_loss | -87.5137 |
| avg_hold_time_bars | 8.7940 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
