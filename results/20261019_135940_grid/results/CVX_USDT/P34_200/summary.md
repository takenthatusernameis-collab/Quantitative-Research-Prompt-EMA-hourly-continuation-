# EMA Hourly Continuation — CVX/USDT P34_200

**Symbol:** CVX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8298 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -2.7149 |
| sortino_ratio | -0.7231 |
| max_drawdown | 0.5822 |
| cagr | -0.2920 |
| net_avg_win | 64.6111 |
| net_avg_loss | -82.0634 |
| avg_hold_time_bars | 30.5276 |
| exposure | 0.5023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
