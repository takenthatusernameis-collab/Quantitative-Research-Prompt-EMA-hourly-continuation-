# EMA Hourly Continuation — MTL/USDT P20_200

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5973 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8786 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -3.1492 |
| sortino_ratio | -0.8265 |
| max_drawdown | 0.6426 |
| cagr | -0.3289 |
| net_avg_win | 59.1821 |
| net_avg_loss | -81.2008 |
| avg_hold_time_bars | 41.3994 |
| exposure | 0.6613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
