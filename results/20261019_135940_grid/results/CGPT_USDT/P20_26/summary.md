# EMA Hourly Continuation — CGPT/USDT P20_26

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1142 |
| net_profit_factor | 0.2363 |
| net_win_rate | 0.3520 |
| gross_profit_factor | 0.6985 |
| gross_win_rate | 0.3897 |
| sharpe_ratio | -14.0389 |
| sortino_ratio | -6.8738 |
| max_drawdown | 0.9999 |
| cagr | -0.9745 |
| net_avg_win | 7.6946 |
| net_avg_loss | -17.6922 |
| avg_hold_time_bars | 2.0385 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
