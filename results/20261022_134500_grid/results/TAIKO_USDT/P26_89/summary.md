# EMA Hourly Continuation — TAIKO/USDT P26_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5875 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -4.5162 |
| sortino_ratio | -1.6430 |
| max_drawdown | 0.8553 |
| cagr | -0.5461 |
| net_avg_win | 40.4744 |
| net_avg_loss | -61.6546 |
| avg_hold_time_bars | 10.2266 |
| exposure | 0.3100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
