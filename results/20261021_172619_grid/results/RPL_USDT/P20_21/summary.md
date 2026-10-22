# EMA Hourly Continuation — RPL/USDT P20_21

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -3.4454 |
| sortino_ratio | -0.8801 |
| max_drawdown | 0.6463 |
| cagr | -0.3368 |
| net_avg_win | 59.3357 |
| net_avg_loss | -84.2444 |
| avg_hold_time_bars | 5.0652 |
| exposure | 0.0738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
