# EMA Hourly Continuation — YGG/USDT P26_200

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.8797 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0345 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -0.6991 |
| sortino_ratio | -0.1790 |
| max_drawdown | 0.2602 |
| cagr | -0.0818 |
| net_avg_win | 86.8553 |
| net_avg_loss | -102.5053 |
| avg_hold_time_bars | 37.9281 |
| exposure | 0.5492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
