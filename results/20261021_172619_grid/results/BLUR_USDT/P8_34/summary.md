# EMA Hourly Continuation — BLUR/USDT P8_34

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -3.1872 |
| sortino_ratio | -1.2803 |
| max_drawdown | 0.7808 |
| cagr | -0.4444 |
| net_avg_win | 49.9800 |
| net_avg_loss | -64.6664 |
| avg_hold_time_bars | 8.3258 |
| exposure | 0.2995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
