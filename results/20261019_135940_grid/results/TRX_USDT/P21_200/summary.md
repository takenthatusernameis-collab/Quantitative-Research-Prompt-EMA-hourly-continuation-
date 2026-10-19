# EMA Hourly Continuation — TRX/USDT P21_200

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.4245 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.9298 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -5.6549 |
| sortino_ratio | -1.5623 |
| max_drawdown | 0.8764 |
| cagr | -0.5617 |
| net_avg_win | 37.4742 |
| net_avg_loss | -69.3401 |
| avg_hold_time_bars | 32.9028 |
| exposure | 0.5848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
