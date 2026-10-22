# EMA Hourly Continuation — AERO/USDT P20_50

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.5204 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -5.6043 |
| sortino_ratio | -2.3551 |
| max_drawdown | 0.9462 |
| cagr | -0.6851 |
| net_avg_win | 24.1819 |
| net_avg_loss | -41.2213 |
| avg_hold_time_bars | 5.0665 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
