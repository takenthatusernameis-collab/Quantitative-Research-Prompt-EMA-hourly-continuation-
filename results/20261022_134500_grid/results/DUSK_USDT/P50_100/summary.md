# EMA Hourly Continuation — DUSK/USDT P50_100

**Symbol:** DUSK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5734 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9160 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -4.2342 |
| sortino_ratio | -1.5086 |
| max_drawdown | 0.8426 |
| cagr | -0.5163 |
| net_avg_win | 37.1949 |
| net_avg_loss | -57.6432 |
| avg_hold_time_bars | 5.8587 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
