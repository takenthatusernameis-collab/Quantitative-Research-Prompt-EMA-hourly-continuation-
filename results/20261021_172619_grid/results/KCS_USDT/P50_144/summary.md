# EMA Hourly Continuation — KCS/USDT P50_144

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.5375 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8960 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.1599 |
| sortino_ratio | -0.8123 |
| max_drawdown | 0.6138 |
| cagr | -0.3105 |
| net_avg_win | 46.0891 |
| net_avg_loss | -78.5642 |
| avg_hold_time_bars | 21.1812 |
| exposure | 0.3081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
