# EMA Hourly Continuation — IMX/USDT P21_34

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.3308 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.6848 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -9.6300 |
| sortino_ratio | -4.4922 |
| max_drawdown | 0.9968 |
| cagr | -0.8973 |
| net_avg_win | 10.5515 |
| net_avg_loss | -23.5315 |
| avg_hold_time_bars | 2.6918 |
| exposure | 0.1340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
