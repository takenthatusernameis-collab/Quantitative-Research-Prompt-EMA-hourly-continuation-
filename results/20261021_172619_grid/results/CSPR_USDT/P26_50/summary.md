# EMA Hourly Continuation — CSPR/USDT P26_50

**Symbol:** CSPR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.8283 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -2.9951 |
| sortino_ratio | -0.8009 |
| max_drawdown | 0.6099 |
| cagr | -0.3077 |
| net_avg_win | 65.5186 |
| net_avg_loss | -82.0714 |
| avg_hold_time_bars | 5.8927 |
| exposure | 0.0948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
