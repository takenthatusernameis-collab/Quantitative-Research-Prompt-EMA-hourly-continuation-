# EMA Hourly Continuation — RLC/USDT P26_200

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.6533 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.6403 |
| sortino_ratio | -0.7554 |
| max_drawdown | 0.6261 |
| cagr | -0.3080 |
| net_avg_win | 55.7424 |
| net_avg_loss | -79.8401 |
| avg_hold_time_bars | 28.8270 |
| exposure | 0.5530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
