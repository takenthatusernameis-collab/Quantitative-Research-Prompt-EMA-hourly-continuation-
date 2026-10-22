# EMA Hourly Continuation — SUPER/USDT P12_26

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1367 |
| net_profit_factor | 0.4939 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -9.2989 |
| sortino_ratio | -4.8483 |
| max_drawdown | 0.9977 |
| cagr | -0.9104 |
| net_avg_win | 15.8853 |
| net_avg_loss | -26.1463 |
| avg_hold_time_bars | 3.0622 |
| exposure | 0.1903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
