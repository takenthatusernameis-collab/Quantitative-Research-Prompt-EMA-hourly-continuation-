# EMA Hourly Continuation — ELON/USDT P89_200

**Symbol:** ELON/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5812 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -3.1532 |
| sortino_ratio | -0.9098 |
| max_drawdown | 0.6646 |
| cagr | -0.3465 |
| net_avg_win | 46.4871 |
| net_avg_loss | -72.5748 |
| avg_hold_time_bars | 9.9150 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
