# EMA Hourly Continuation — EGLD/USDT P34_55

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.6728 |
| sortino_ratio | -0.7222 |
| max_drawdown | 0.5836 |
| cagr | -0.2801 |
| net_avg_win | 55.0989 |
| net_avg_loss | -82.1949 |
| avg_hold_time_bars | 6.3079 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
