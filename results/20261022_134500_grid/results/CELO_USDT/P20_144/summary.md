# EMA Hourly Continuation — CELO/USDT P20_144

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.8039 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.1109 |
| gross_win_rate | 0.5229 |
| sharpe_ratio | -1.5066 |
| sortino_ratio | -0.4491 |
| max_drawdown | 0.4582 |
| cagr | -0.1881 |
| net_avg_win | 74.7972 |
| net_avg_loss | -98.3149 |
| avg_hold_time_bars | 29.4060 |
| exposure | 0.5802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
