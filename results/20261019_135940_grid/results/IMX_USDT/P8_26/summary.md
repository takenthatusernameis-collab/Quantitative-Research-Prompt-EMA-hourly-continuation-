# EMA Hourly Continuation — IMX/USDT P8_26

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1471 |
| net_profit_factor | 0.5338 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -8.6053 |
| sortino_ratio | -4.6058 |
| max_drawdown | 0.9971 |
| cagr | -0.8992 |
| net_avg_win | 16.8640 |
| net_avg_loss | -26.9349 |
| avg_hold_time_bars | 4.0768 |
| exposure | 0.2714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
