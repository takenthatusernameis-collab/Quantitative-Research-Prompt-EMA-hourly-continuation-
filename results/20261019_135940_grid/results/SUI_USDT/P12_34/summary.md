# EMA Hourly Continuation — SUI/USDT P12_34

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1314 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -9.7240 |
| sortino_ratio | -4.9490 |
| max_drawdown | 0.9981 |
| cagr | -0.9168 |
| net_avg_win | 18.2553 |
| net_avg_loss | -27.0355 |
| avg_hold_time_bars | 3.9848 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
