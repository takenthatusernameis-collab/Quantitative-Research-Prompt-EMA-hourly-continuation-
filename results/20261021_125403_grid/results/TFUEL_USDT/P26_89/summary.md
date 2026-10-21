# EMA Hourly Continuation — TFUEL/USDT P26_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.5292 |
| net_win_rate | 0.4025 |
| gross_profit_factor | 0.6991 |
| gross_win_rate | 0.4025 |
| sharpe_ratio | -5.0282 |
| sortino_ratio | -1.6785 |
| max_drawdown | 0.8608 |
| cagr | -0.5393 |
| net_avg_win | 42.8816 |
| net_avg_loss | -54.5883 |
| avg_hold_time_bars | 10.5975 |
| exposure | 0.2681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
