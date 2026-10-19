# EMA Hourly Continuation — ONDO/USDT P12_50

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1094 |
| net_profit_factor | 0.6083 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -5.8668 |
| sortino_ratio | -2.7208 |
| max_drawdown | 0.9645 |
| cagr | -0.7323 |
| net_avg_win | 29.2246 |
| net_avg_loss | -42.2642 |
| avg_hold_time_bars | 6.4168 |
| exposure | 0.3191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
