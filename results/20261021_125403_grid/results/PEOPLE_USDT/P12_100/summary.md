# EMA Hourly Continuation — PEOPLE/USDT P12_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7517 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8894 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -1.9692 |
| sortino_ratio | -0.5866 |
| max_drawdown | 0.5252 |
| cagr | -0.2370 |
| net_avg_win | 72.0030 |
| net_avg_loss | -85.1410 |
| avg_hold_time_bars | 29.8801 |
| exposure | 0.5976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
