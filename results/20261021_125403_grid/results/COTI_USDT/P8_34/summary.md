# EMA Hourly Continuation — COTI/USDT P8_34

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0286 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.9545 |
| sortino_ratio | -0.7680 |
| max_drawdown | 0.6317 |
| cagr | -0.2986 |
| net_avg_win | 68.4767 |
| net_avg_loss | -85.2015 |
| avg_hold_time_bars | 8.1305 |
| exposure | 0.2775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
