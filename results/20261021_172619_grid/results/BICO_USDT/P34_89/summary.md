# EMA Hourly Continuation — BICO/USDT P34_89

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8185 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -3.0392 |
| sortino_ratio | -0.9645 |
| max_drawdown | 0.6799 |
| cagr | -0.3572 |
| net_avg_win | 51.2800 |
| net_avg_loss | -67.0067 |
| avg_hold_time_bars | 11.2846 |
| exposure | 0.2560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
