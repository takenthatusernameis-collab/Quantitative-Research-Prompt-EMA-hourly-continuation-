# EMA Hourly Continuation — COMP/USDT P20_55

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.4333 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.8553 |
| gross_win_rate | 0.5005 |
| sharpe_ratio | -6.6467 |
| sortino_ratio | -3.0124 |
| max_drawdown | 0.9751 |
| cagr | -0.7677 |
| net_avg_win | 15.1737 |
| net_avg_loss | -31.9601 |
| avg_hold_time_bars | 5.8746 |
| exposure | 0.2748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
