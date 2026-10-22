# EMA Hourly Continuation — EGLD/USDT P21_26

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1198 |
| net_profit_factor | 0.1863 |
| net_win_rate | 0.3531 |
| gross_profit_factor | 0.6692 |
| gross_win_rate | 0.4190 |
| sharpe_ratio | -14.8283 |
| sortino_ratio | -7.5341 |
| max_drawdown | 1.0000 |
| cagr | -0.9820 |
| net_avg_win | 5.4120 |
| net_avg_loss | -15.8566 |
| avg_hold_time_bars | 1.9891 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
