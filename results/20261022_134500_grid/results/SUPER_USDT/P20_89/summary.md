# EMA Hourly Continuation — SUPER/USDT P20_89

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6570 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -3.3688 |
| sortino_ratio | -1.2776 |
| max_drawdown | 0.7938 |
| cagr | -0.4535 |
| net_avg_win | 42.1294 |
| net_avg_loss | -62.5364 |
| avg_hold_time_bars | 12.0348 |
| exposure | 0.3933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
