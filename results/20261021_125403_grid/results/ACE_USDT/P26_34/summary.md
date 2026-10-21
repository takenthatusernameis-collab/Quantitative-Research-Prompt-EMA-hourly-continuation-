# EMA Hourly Continuation — ACE/USDT P26_34

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.6714 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -2.1181 |
| sortino_ratio | -0.5368 |
| max_drawdown | 0.4737 |
| cagr | -0.2201 |
| net_avg_win | 59.4751 |
| net_avg_loss | -90.8594 |
| avg_hold_time_bars | 6.1361 |
| exposure | 0.0877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
