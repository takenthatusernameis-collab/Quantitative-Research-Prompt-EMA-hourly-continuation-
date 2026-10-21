# EMA Hourly Continuation — ID/USDT P26_200

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8760 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0640 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -0.6498 |
| sortino_ratio | -0.1629 |
| max_drawdown | 0.1983 |
| cagr | -0.0745 |
| net_avg_win | 78.8427 |
| net_avg_loss | -97.3530 |
| avg_hold_time_bars | 42.3856 |
| exposure | 0.5870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
