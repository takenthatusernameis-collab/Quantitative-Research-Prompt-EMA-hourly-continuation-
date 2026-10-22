# EMA Hourly Continuation — SQD/USDT P26_89

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.9025 |
| net_win_rate | 0.5189 |
| gross_profit_factor | 1.0773 |
| gross_win_rate | 0.5189 |
| sharpe_ratio | -0.6962 |
| sortino_ratio | -0.2158 |
| max_drawdown | 0.3296 |
| cagr | -0.0989 |
| net_avg_win | 88.8134 |
| net_avg_loss | -106.1500 |
| avg_hold_time_bars | 13.3853 |
| exposure | 0.2825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
