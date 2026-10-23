# EMA Hourly Continuation — PIXEL/USDT P50_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 884 |
| net_profit_factor | 0.3289 |
| net_win_rate | 0.3903 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -10.6281 |
| sortino_ratio | -4.5268 |
| max_drawdown | 0.9975 |
| cagr | -0.9049 |
| net_avg_win | 14.1695 |
| net_avg_loss | -27.5733 |
| avg_hold_time_bars | 2.1991 |
| exposure | 0.0880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
