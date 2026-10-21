# EMA Hourly Continuation — ENA/USDT P100_144

**Symbol:** ENA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 1.1258 |
| net_win_rate | 0.5852 |
| gross_profit_factor | 1.3987 |
| gross_win_rate | 0.5852 |
| sharpe_ratio | 0.5255 |
| sortino_ratio | 0.1025 |
| max_drawdown | 0.0920 |
| cagr | 0.0412 |
| net_avg_win | 92.5858 |
| net_avg_loss | -116.0345 |
| avg_hold_time_bars | 6.4205 |
| exposure | 0.0514 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
