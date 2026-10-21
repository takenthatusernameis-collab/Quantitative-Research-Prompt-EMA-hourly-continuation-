# EMA Hourly Continuation — KAS/USDT P21_26

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.9970 |
| net_win_rate | 0.5859 |
| gross_profit_factor | 1.3996 |
| gross_win_rate | 0.5859 |
| sharpe_ratio | 0.0245 |
| sortino_ratio | 0.0041 |
| max_drawdown | 0.1207 |
| cagr | -0.0008 |
| net_avg_win | 87.1627 |
| net_avg_loss | -123.7088 |
| avg_hold_time_bars | 4.9609 |
| exposure | 0.0289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
