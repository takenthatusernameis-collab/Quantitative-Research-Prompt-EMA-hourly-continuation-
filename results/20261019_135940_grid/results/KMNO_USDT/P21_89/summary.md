# EMA Hourly Continuation — KMNO/USDT P21_89

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5988 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8751 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -4.3981 |
| sortino_ratio | -1.5271 |
| max_drawdown | 0.8376 |
| cagr | -0.5178 |
| net_avg_win | 46.3529 |
| net_avg_loss | -63.4810 |
| avg_hold_time_bars | 13.4858 |
| exposure | 0.3717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
