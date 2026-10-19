# EMA Hourly Continuation — AERO/USDT P12_144

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7906 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0687 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.8444 |
| sortino_ratio | -0.5724 |
| max_drawdown | 0.5646 |
| cagr | -0.2426 |
| net_avg_win | 75.8460 |
| net_avg_loss | -99.5187 |
| avg_hold_time_bars | 28.7984 |
| exposure | 0.6427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
