# EMA Hourly Continuation — MOG/USDT P26_89

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.8129 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.3594 |
| sortino_ratio | -0.4105 |
| max_drawdown | 0.4209 |
| cagr | -0.1736 |
| net_avg_win | 76.2470 |
| net_avg_loss | -91.9790 |
| avg_hold_time_bars | 13.6471 |
| exposure | 0.2768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
