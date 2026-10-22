# EMA Hourly Continuation — MOODENG/USDT P12_26

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.8874 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.5685 |
| sortino_ratio | -0.7951 |
| max_drawdown | 0.5628 |
| cagr | -0.3059 |
| net_avg_win | 61.1991 |
| net_avg_loss | -81.5386 |
| avg_hold_time_bars | 6.0284 |
| exposure | 0.1291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
