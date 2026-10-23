# EMA Hourly Continuation — WAVES/USDT P26_55

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1051 |
| net_profit_factor | 0.3916 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.8620 |
| gross_win_rate | 0.4310 |
| sharpe_ratio | -10.6386 |
| sortino_ratio | -4.8964 |
| max_drawdown | 0.9981 |
| cagr | -0.9174 |
| net_avg_win | 15.4819 |
| net_avg_loss | -25.7954 |
| avg_hold_time_bars | 3.9277 |
| exposure | 0.1876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
