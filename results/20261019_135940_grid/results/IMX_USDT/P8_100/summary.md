# EMA Hourly Continuation — IMX/USDT P8_100

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7404 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0310 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -2.1331 |
| sortino_ratio | -0.7454 |
| max_drawdown | 0.6068 |
| cagr | -0.2989 |
| net_avg_win | 53.9247 |
| net_avg_loss | -76.2372 |
| avg_hold_time_bars | 24.1258 |
| exposure | 0.6681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
