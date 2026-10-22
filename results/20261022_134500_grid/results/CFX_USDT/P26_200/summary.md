# EMA Hourly Continuation — CFX/USDT P26_200

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6765 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.5393 |
| sortino_ratio | -0.7275 |
| max_drawdown | 0.5953 |
| cagr | -0.2934 |
| net_avg_win | 60.2383 |
| net_avg_loss | -84.0558 |
| avg_hold_time_bars | 28.6995 |
| exposure | 0.5427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
