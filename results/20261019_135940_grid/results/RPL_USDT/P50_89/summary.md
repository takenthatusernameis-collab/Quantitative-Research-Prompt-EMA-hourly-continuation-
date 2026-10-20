# EMA Hourly Continuation — RPL/USDT P50_89

**Symbol:** RPL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.5510 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8827 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -4.7064 |
| sortino_ratio | -1.6621 |
| max_drawdown | 0.8626 |
| cagr | -0.5418 |
| net_avg_win | 36.9230 |
| net_avg_loss | -56.5297 |
| avg_hold_time_bars | 6.6400 |
| exposure | 0.1878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
