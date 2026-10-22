# EMA Hourly Continuation — FLOKI/USDT P26_34

**Symbol:** FLOKI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1172 |
| net_profit_factor | 0.3247 |
| net_win_rate | 0.3643 |
| gross_profit_factor | 0.6821 |
| gross_win_rate | 0.3942 |
| sharpe_ratio | -13.5819 |
| sortino_ratio | -6.6913 |
| max_drawdown | 0.9999 |
| cagr | -0.9717 |
| net_avg_win | 11.2574 |
| net_avg_loss | -19.8733 |
| avg_hold_time_bars | 1.9778 |
| exposure | 0.1054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
