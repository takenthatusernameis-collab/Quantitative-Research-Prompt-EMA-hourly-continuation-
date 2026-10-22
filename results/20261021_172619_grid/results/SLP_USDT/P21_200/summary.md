# EMA Hourly Continuation — SLP/USDT P21_200

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8682 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0637 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -0.8841 |
| sortino_ratio | -0.2369 |
| max_drawdown | 0.3486 |
| cagr | -0.1057 |
| net_avg_win | 89.9903 |
| net_avg_loss | -109.1395 |
| avg_hold_time_bars | 38.1117 |
| exposure | 0.6046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
