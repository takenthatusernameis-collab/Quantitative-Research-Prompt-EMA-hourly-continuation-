# EMA Hourly Continuation — IMX/USDT P8_12

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1740 |
| net_profit_factor | 0.2637 |
| net_win_rate | 0.3943 |
| gross_profit_factor | 0.7956 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -15.6822 |
| sortino_ratio | -9.3453 |
| max_drawdown | 1.0000 |
| cagr | -0.9928 |
| net_avg_win | 5.2213 |
| net_avg_loss | -12.8859 |
| avg_hold_time_bars | 1.9443 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
