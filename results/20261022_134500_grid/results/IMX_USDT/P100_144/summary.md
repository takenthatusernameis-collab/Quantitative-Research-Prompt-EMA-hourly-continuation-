# EMA Hourly Continuation — IMX/USDT P100_144

**Symbol:** IMX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -4.4974 |
| sortino_ratio | -1.4319 |
| max_drawdown | 0.8382 |
| cagr | -0.5018 |
| net_avg_win | 38.5455 |
| net_avg_loss | -64.5757 |
| avg_hold_time_bars | 4.0858 |
| exposure | 0.0948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
