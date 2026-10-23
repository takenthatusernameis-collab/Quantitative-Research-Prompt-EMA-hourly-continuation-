# EMA Hourly Continuation — ALEX/USDT P12_89

**Symbol:** ALEX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.9637 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -3.7967 |
| sortino_ratio | -1.2208 |
| max_drawdown | 0.7907 |
| cagr | -0.4460 |
| net_avg_win | 55.2059 |
| net_avg_loss | -73.4849 |
| avg_hold_time_bars | 25.0964 |
| exposure | 0.6035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
