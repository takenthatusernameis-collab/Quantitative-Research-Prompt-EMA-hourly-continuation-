# EMA Hourly Continuation — ALEX/USDT P20_26

**Symbol:** ALEX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.2643 |
| net_win_rate | 0.3030 |
| gross_profit_factor | 0.7442 |
| gross_win_rate | 0.3364 |
| sharpe_ratio | -14.9726 |
| sortino_ratio | -7.0919 |
| max_drawdown | 0.9999 |
| cagr | -0.9799 |
| net_avg_win | 11.0193 |
| net_avg_loss | -18.1223 |
| avg_hold_time_bars | 2.6691 |
| exposure | 0.1305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
