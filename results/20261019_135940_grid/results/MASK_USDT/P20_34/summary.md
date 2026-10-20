# EMA Hourly Continuation — MASK/USDT P20_34

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.2713 |
| net_win_rate | 0.3943 |
| gross_profit_factor | 0.7102 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -11.9234 |
| sortino_ratio | -5.7701 |
| max_drawdown | 0.9994 |
| cagr | -0.9489 |
| net_avg_win | 8.2158 |
| net_avg_loss | -19.7070 |
| avg_hold_time_bars | 3.3116 |
| exposure | 0.1730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
