# EMA Hourly Continuation — ACE/USDT P21_34

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 880 |
| net_profit_factor | 0.4068 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -6.7238 |
| sortino_ratio | -2.8230 |
| max_drawdown | 0.9679 |
| cagr | -0.7422 |
| net_avg_win | 16.3369 |
| net_avg_loss | -34.3998 |
| avg_hold_time_bars | 3.9614 |
| exposure | 0.1578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
