# EMA Hourly Continuation — FIDA/USDT P26_89

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.2132 |
| sortino_ratio | -0.7046 |
| max_drawdown | 0.5821 |
| cagr | -0.2765 |
| net_avg_win | 54.8052 |
| net_avg_loss | -74.3258 |
| avg_hold_time_bars | 13.7916 |
| exposure | 0.3114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
