# EMA Hourly Continuation — WEMIX/USDT P26_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.3419 |
| net_win_rate | 0.3110 |
| gross_profit_factor | 0.5021 |
| gross_win_rate | 0.3196 |
| sharpe_ratio | -8.6542 |
| sortino_ratio | -2.9481 |
| max_drawdown | 0.9742 |
| cagr | -0.7657 |
| net_avg_win | 27.9541 |
| net_avg_loss | -36.9034 |
| avg_hold_time_bars | 23.3385 |
| exposure | 0.6174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
