# EMA Hourly Continuation — TNSR/USDT P34_100

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.7291 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0430 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -2.9635 |
| sortino_ratio | -1.0524 |
| max_drawdown | 0.7295 |
| cagr | -0.3938 |
| net_avg_win | 61.2830 |
| net_avg_loss | -82.7345 |
| avg_hold_time_bars | 10.1197 |
| exposure | 0.2908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
