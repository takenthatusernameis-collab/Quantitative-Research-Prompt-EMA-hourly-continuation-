# EMA Hourly Continuation — SAFE/USDT P21_55

**Symbol:** SAFE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9622 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.1814 |
| sortino_ratio | -0.7129 |
| max_drawdown | 0.5862 |
| cagr | -0.2789 |
| net_avg_win | 61.2949 |
| net_avg_loss | -80.6231 |
| avg_hold_time_bars | 8.9498 |
| exposure | 0.2123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
