# EMA Hourly Continuation — BAND/USDT P12_26

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -3.6755 |
| sortino_ratio | -1.3487 |
| max_drawdown | 0.7902 |
| cagr | -0.4615 |
| net_avg_win | 51.3630 |
| net_avg_loss | -71.8538 |
| avg_hold_time_bars | 5.7215 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
