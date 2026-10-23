# EMA Hourly Continuation — SKL/USDT P34_89

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -4.2255 |
| sortino_ratio | -1.5630 |
| max_drawdown | 0.8514 |
| cagr | -0.5198 |
| net_avg_win | 39.3313 |
| net_avg_loss | -58.7731 |
| avg_hold_time_bars | 8.7511 |
| exposure | 0.2701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
