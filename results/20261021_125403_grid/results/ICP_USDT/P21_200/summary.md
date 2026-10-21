# EMA Hourly Continuation — ICP/USDT P21_200

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8700 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0254 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -0.7115 |
| sortino_ratio | -0.1726 |
| max_drawdown | 0.2297 |
| cagr | -0.0787 |
| net_avg_win | 85.2620 |
| net_avg_loss | -101.4760 |
| avg_hold_time_bars | 48.8676 |
| exposure | 0.6375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
