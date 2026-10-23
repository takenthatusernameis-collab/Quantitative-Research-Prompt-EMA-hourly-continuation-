# EMA Hourly Continuation — GLM/USDT P8_100

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.6138 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.8988 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -4.0794 |
| sortino_ratio | -1.5136 |
| max_drawdown | 0.8424 |
| cagr | -0.5115 |
| net_avg_win | 40.8022 |
| net_avg_loss | -59.0327 |
| avg_hold_time_bars | 20.5658 |
| exposure | 0.6460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
