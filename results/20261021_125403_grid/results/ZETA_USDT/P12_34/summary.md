# EMA Hourly Continuation — ZETA/USDT P12_34

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.7121 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9553 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.8729 |
| sortino_ratio | -1.0610 |
| max_drawdown | 0.7128 |
| cagr | -0.3844 |
| net_avg_win | 53.3982 |
| net_avg_loss | -71.6982 |
| avg_hold_time_bars | 6.7354 |
| exposure | 0.2039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
