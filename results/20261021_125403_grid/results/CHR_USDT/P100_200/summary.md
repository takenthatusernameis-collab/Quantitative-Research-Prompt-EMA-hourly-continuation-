# EMA Hourly Continuation — CHR/USDT P100_200

**Symbol:** CHR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -1.5312 |
| sortino_ratio | -0.3810 |
| max_drawdown | 0.3624 |
| cagr | -0.1614 |
| net_avg_win | 69.6689 |
| net_avg_loss | -88.5189 |
| avg_hold_time_bars | 12.4623 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
