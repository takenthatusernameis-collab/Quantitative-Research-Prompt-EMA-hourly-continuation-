# EMA Hourly Continuation — POLYX/USDT P8_50

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.6275 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9872 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -5.1117 |
| sortino_ratio | -2.2816 |
| max_drawdown | 0.9386 |
| cagr | -0.6660 |
| net_avg_win | 32.4544 |
| net_avg_loss | -48.1536 |
| avg_hold_time_bars | 10.3800 |
| exposure | 0.4756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
