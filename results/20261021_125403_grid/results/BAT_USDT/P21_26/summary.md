# EMA Hourly Continuation — BAT/USDT P21_26

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.5006 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8535 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -3.5549 |
| sortino_ratio | -0.8551 |
| max_drawdown | 0.6309 |
| cagr | -0.3261 |
| net_avg_win | 49.6347 |
| net_avg_loss | -82.3045 |
| avg_hold_time_bars | 4.5214 |
| exposure | 0.0575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
