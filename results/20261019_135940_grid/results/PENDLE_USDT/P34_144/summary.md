# EMA Hourly Continuation — PENDLE/USDT P34_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6088 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8872 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.3109 |
| sortino_ratio | -1.0598 |
| max_drawdown | 0.7390 |
| cagr | -0.3964 |
| net_avg_win | 46.1963 |
| net_avg_loss | -66.7806 |
| avg_hold_time_bars | 18.3752 |
| exposure | 0.4318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
