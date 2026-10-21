# EMA Hourly Continuation — AXS/USDT P20_21

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 106 |
| net_profit_factor | 0.7728 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1297 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -0.8539 |
| sortino_ratio | -0.1268 |
| max_drawdown | 0.2086 |
| cagr | -0.0565 |
| net_avg_win | 82.9033 |
| net_avg_loss | -120.1477 |
| avg_hold_time_bars | 5.2925 |
| exposure | 0.0254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
