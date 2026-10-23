# EMA Hourly Continuation — AXL/USDT P50_100

**Symbol:** AXL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.5375 |
| net_win_rate | 0.4327 |
| gross_profit_factor | 0.8233 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -5.6979 |
| sortino_ratio | -2.1243 |
| max_drawdown | 0.9228 |
| cagr | -0.6343 |
| net_avg_win | 35.4437 |
| net_avg_loss | -50.2865 |
| avg_hold_time_bars | 5.9284 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
