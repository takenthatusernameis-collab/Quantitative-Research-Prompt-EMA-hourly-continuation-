# EMA Hourly Continuation — YGG/USDT P8_21

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0677 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -2.3467 |
| sortino_ratio | -0.8827 |
| max_drawdown | 0.6788 |
| cagr | -0.3330 |
| net_avg_win | 68.5019 |
| net_avg_loss | -89.8677 |
| avg_hold_time_bars | 5.2195 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
