# EMA Hourly Continuation — AEVO/USDT P20_200

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.9939 |
| net_win_rate | 0.5441 |
| gross_profit_factor | 1.1865 |
| gross_win_rate | 0.5441 |
| sharpe_ratio | 0.0169 |
| sortino_ratio | 0.0039 |
| max_drawdown | 0.2231 |
| cagr | -0.0035 |
| net_avg_win | 99.9240 |
| net_avg_loss | -119.9695 |
| avg_hold_time_bars | 58.0690 |
| exposure | 0.6858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
