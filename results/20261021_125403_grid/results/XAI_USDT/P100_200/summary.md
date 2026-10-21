# EMA Hourly Continuation — XAI/USDT P100_200

**Symbol:** XAI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.8623 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0848 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -0.7508 |
| sortino_ratio | -0.1767 |
| max_drawdown | 0.2873 |
| cagr | -0.0797 |
| net_avg_win | 84.8226 |
| net_avg_loss | -106.8242 |
| avg_hold_time_bars | 14.2360 |
| exposure | 0.1728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
