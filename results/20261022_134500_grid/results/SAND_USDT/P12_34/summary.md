# EMA Hourly Continuation — SAND/USDT P12_34

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1273 |
| net_profit_factor | 0.3617 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.8186 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -10.0996 |
| sortino_ratio | -5.0665 |
| max_drawdown | 0.9984 |
| cagr | -0.9228 |
| net_avg_win | 10.5172 |
| net_avg_loss | -21.2818 |
| avg_hold_time_bars | 4.0346 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
