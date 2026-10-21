# EMA Hourly Continuation — XRP/USDT P50_100

**Symbol:** XRP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -2.1295 |
| sortino_ratio | -0.5361 |
| max_drawdown | 0.4718 |
| cagr | -0.2158 |
| net_avg_win | 55.8376 |
| net_avg_loss | -89.1239 |
| avg_hold_time_bars | 10.5344 |
| exposure | 0.1460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
