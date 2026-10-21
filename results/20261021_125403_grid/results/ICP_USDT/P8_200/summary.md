# EMA Hourly Continuation — ICP/USDT P8_200

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.9260 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0740 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.3591 |
| sortino_ratio | -0.0840 |
| max_drawdown | 0.1715 |
| cagr | -0.0413 |
| net_avg_win | 91.1619 |
| net_avg_loss | -106.9699 |
| avg_hold_time_bars | 66.1811 |
| exposure | 0.7972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
