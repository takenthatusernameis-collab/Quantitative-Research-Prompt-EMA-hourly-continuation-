# EMA Hourly Continuation — IMX/USDT P8_100

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.9656 |
| net_win_rate | 0.5355 |
| gross_profit_factor | 1.1457 |
| gross_win_rate | 0.5355 |
| sharpe_ratio | -0.1655 |
| sortino_ratio | -0.0515 |
| max_drawdown | 0.1665 |
| cagr | -0.0312 |
| net_avg_win | 86.4046 |
| net_avg_loss | -103.1590 |
| avg_hold_time_bars | 31.2280 |
| exposure | 0.6571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
