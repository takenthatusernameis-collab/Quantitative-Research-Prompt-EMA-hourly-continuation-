# EMA Hourly Continuation — ENS/USDT P21_100

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6498 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9643 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -3.5357 |
| sortino_ratio | -1.2551 |
| max_drawdown | 0.8027 |
| cagr | -0.4541 |
| net_avg_win | 46.6122 |
| net_avg_loss | -67.8115 |
| avg_hold_time_bars | 15.0828 |
| exposure | 0.4388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
