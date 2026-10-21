# EMA Hourly Continuation — CELR/USDT P20_89

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.5101 |
| sortino_ratio | -0.8419 |
| max_drawdown | 0.6498 |
| cagr | -0.3214 |
| net_avg_win | 62.7263 |
| net_avg_loss | -78.5637 |
| avg_hold_time_bars | 15.8219 |
| exposure | 0.3981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
