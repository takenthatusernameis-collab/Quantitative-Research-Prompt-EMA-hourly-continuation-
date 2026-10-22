# EMA Hourly Continuation — STRK/USDT P21_89

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.9453 |
| sortino_ratio | -1.4843 |
| max_drawdown | 0.8363 |
| cagr | -0.5071 |
| net_avg_win | 44.6837 |
| net_avg_loss | -63.2426 |
| avg_hold_time_bars | 11.2070 |
| exposure | 0.3642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
