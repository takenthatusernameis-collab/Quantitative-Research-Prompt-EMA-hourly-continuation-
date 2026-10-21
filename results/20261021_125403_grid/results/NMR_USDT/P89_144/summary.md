# EMA Hourly Continuation — NMR/USDT P89_144

**Symbol:** NMR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 0.9982 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -1.8171 |
| sortino_ratio | -0.4489 |
| max_drawdown | 0.4539 |
| cagr | -0.1857 |
| net_avg_win | 66.0811 |
| net_avg_loss | -94.3939 |
| avg_hold_time_bars | 8.7297 |
| exposure | 0.1175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
