# EMA Hourly Continuation — YGG/USDT P20_100

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.5990 |
| sortino_ratio | -0.5075 |
| max_drawdown | 0.5369 |
| cagr | -0.2094 |
| net_avg_win | 82.1197 |
| net_avg_loss | -98.3625 |
| avg_hold_time_bars | 18.6586 |
| exposure | 0.4179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
