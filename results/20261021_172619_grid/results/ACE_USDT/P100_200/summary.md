# EMA Hourly Continuation — ACE/USDT P100_200

**Symbol:** ACE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.8029 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0189 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.0270 |
| sortino_ratio | -0.2403 |
| max_drawdown | 0.3113 |
| cagr | -0.1052 |
| net_avg_win | 73.2388 |
| net_avg_loss | -94.7018 |
| avg_hold_time_bars | 13.4345 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
