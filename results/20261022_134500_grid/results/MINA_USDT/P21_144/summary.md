# EMA Hourly Continuation — MINA/USDT P21_144

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.7381 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0601 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.9487 |
| sortino_ratio | -0.5933 |
| max_drawdown | 0.5539 |
| cagr | -0.2469 |
| net_avg_win | 59.8165 |
| net_avg_loss | -86.8316 |
| avg_hold_time_bars | 27.5000 |
| exposure | 0.5800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
