# EMA Hourly Continuation — ATOM/USDT P55_89

**Symbol:** ATOM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6695 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.8982 |
| sortino_ratio | -0.4467 |
| max_drawdown | 0.4097 |
| cagr | -0.1840 |
| net_avg_win | 60.8941 |
| net_avg_loss | -89.6122 |
| avg_hold_time_bars | 7.0299 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
