# EMA Hourly Continuation — GALA/USDT P8_34

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.7486 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -2.5254 |
| sortino_ratio | -0.9557 |
| max_drawdown | 0.6797 |
| cagr | -0.3557 |
| net_avg_win | 58.3803 |
| net_avg_loss | -73.8660 |
| avg_hold_time_bars | 8.7817 |
| exposure | 0.2798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
