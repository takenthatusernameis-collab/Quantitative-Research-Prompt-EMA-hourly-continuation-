# EMA Hourly Continuation — AAVE/USDT P26_89

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5485 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9000 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -4.7221 |
| sortino_ratio | -1.7284 |
| max_drawdown | 0.8921 |
| cagr | -0.5710 |
| net_avg_win | 33.0215 |
| net_avg_loss | -54.6359 |
| avg_hold_time_bars | 9.7592 |
| exposure | 0.3021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
