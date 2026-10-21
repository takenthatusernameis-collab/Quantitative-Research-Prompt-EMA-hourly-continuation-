# EMA Hourly Continuation — AXS/USDT P100_200

**Symbol:** AXS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.9452 |
| net_win_rate | 0.5564 |
| gross_profit_factor | 1.2390 |
| gross_win_rate | 0.5564 |
| sharpe_ratio | -0.2235 |
| sortino_ratio | -0.0519 |
| max_drawdown | 0.1623 |
| cagr | -0.0273 |
| net_avg_win | 81.4657 |
| net_avg_loss | -108.1156 |
| avg_hold_time_bars | 10.8599 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
