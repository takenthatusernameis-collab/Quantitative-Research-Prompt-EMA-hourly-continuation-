# EMA Hourly Continuation — RSR/USDT P21_100

**Symbol:** RSR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8516 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.0811 |
| sortino_ratio | -0.3306 |
| max_drawdown | 0.3601 |
| cagr | -0.1437 |
| net_avg_win | 80.4772 |
| net_avg_loss | -96.6060 |
| avg_hold_time_bars | 19.4154 |
| exposure | 0.4015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
