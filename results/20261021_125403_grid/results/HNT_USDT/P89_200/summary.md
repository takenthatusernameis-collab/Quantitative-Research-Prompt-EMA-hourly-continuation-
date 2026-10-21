# EMA Hourly Continuation — HNT/USDT P89_200

**Symbol:** HNT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6655 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.8037 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -2.1968 |
| sortino_ratio | -0.5373 |
| max_drawdown | 0.4932 |
| cagr | -0.2195 |
| net_avg_win | 69.3068 |
| net_avg_loss | -83.9474 |
| avg_hold_time_bars | 16.3087 |
| exposure | 0.2209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
