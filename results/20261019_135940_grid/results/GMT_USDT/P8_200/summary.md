# EMA Hourly Continuation — GMT/USDT P8_200

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0495 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -1.6191 |
| sortino_ratio | -0.4086 |
| max_drawdown | 0.4965 |
| cagr | -0.1787 |
| net_avg_win | 58.9819 |
| net_avg_loss | -85.9095 |
| avg_hold_time_bars | 57.1335 |
| exposure | 0.8362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
