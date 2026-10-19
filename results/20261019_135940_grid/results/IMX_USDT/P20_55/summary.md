# EMA Hourly Continuation — IMX/USDT P20_55

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.5382 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -5.4787 |
| sortino_ratio | -2.3172 |
| max_drawdown | 0.9453 |
| cagr | -0.6789 |
| net_avg_win | 25.4403 |
| net_avg_loss | -42.0179 |
| avg_hold_time_bars | 5.8431 |
| exposure | 0.2427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
