# EMA Hourly Continuation — LINK/USDT P12_100

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9916 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -4.2102 |
| sortino_ratio | -1.4490 |
| max_drawdown | 0.8383 |
| cagr | -0.5080 |
| net_avg_win | 52.6894 |
| net_avg_loss | -73.3055 |
| avg_hold_time_bars | 20.5140 |
| exposure | 0.5641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
