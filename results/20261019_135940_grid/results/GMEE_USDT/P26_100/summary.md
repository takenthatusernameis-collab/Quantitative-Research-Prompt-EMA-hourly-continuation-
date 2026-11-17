# EMA Hourly Continuation — GMEE/USDT P26_100

**Symbol:** GMEE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5909 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8267 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -4.3371 |
| sortino_ratio | -1.5281 |
| max_drawdown | 0.8498 |
| cagr | -0.5187 |
| net_avg_win | 42.7596 |
| net_avg_loss | -59.2207 |
| avg_hold_time_bars | 13.2662 |
| exposure | 0.3805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
