# EMA Hourly Continuation — DOGE/USDT P8_26

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.7386 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -2.3481 |
| sortino_ratio | -0.7953 |
| max_drawdown | 0.6317 |
| cagr | -0.3058 |
| net_avg_win | 60.7801 |
| net_avg_loss | -82.5873 |
| avg_hold_time_bars | 6.7738 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
