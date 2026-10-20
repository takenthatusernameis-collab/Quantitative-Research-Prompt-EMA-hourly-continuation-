# EMA Hourly Continuation — POKT/USDT P50_100

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.5040 |
| net_win_rate | 0.4107 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -6.8943 |
| sortino_ratio | -2.6132 |
| max_drawdown | 0.9610 |
| cagr | -0.7197 |
| net_avg_win | 32.6101 |
| net_avg_loss | -45.0961 |
| avg_hold_time_bars | 6.5385 |
| exposure | 0.2154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
