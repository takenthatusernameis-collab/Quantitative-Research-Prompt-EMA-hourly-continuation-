# EMA Hourly Continuation — KAVA/USDT P20_55

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.9947 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -8.3834 |
| sortino_ratio | -3.7507 |
| max_drawdown | 0.9912 |
| cagr | -0.8464 |
| net_avg_win | 25.9549 |
| net_avg_loss | -37.6596 |
| avg_hold_time_bars | 6.0219 |
| exposure | 0.2745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
