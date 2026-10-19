# EMA Hourly Continuation — DOGE/USDT P20_89

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.5315 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -5.5591 |
| sortino_ratio | -2.0552 |
| max_drawdown | 0.9203 |
| cagr | -0.6295 |
| net_avg_win | 33.6808 |
| net_avg_loss | -51.3940 |
| avg_hold_time_bars | 12.4928 |
| exposure | 0.3918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
