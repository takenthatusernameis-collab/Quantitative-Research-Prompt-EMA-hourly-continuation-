# EMA Hourly Continuation — BAT/USDT P21_50

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6323 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9283 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -3.4549 |
| sortino_ratio | -1.2251 |
| max_drawdown | 0.7673 |
| cagr | -0.4294 |
| net_avg_win | 43.9023 |
| net_avg_loss | -64.8291 |
| avg_hold_time_bars | 6.7896 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
