# EMA Hourly Continuation — XDC/USDT P50_200

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7636 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0623 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -1.5397 |
| sortino_ratio | -0.4105 |
| max_drawdown | 0.4165 |
| cagr | -0.1728 |
| net_avg_win | 68.3762 |
| net_avg_loss | -95.9791 |
| avg_hold_time_bars | 18.0867 |
| exposure | 0.2845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
