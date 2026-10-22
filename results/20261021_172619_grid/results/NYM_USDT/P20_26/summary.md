# EMA Hourly Continuation — NYM/USDT P20_26

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.3325 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.6724 |
| gross_win_rate | 0.4079 |
| sharpe_ratio | -4.5193 |
| sortino_ratio | -0.9821 |
| max_drawdown | 0.6911 |
| cagr | -0.3714 |
| net_avg_win | 37.2716 |
| net_avg_loss | -75.8246 |
| avg_hold_time_bars | 9.1447 |
| exposure | 0.0948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
