# EMA Hourly Continuation — DYDX/USDT P50_89

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6850 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.1114 |
| sortino_ratio | -0.5816 |
| max_drawdown | 0.4959 |
| cagr | -0.2335 |
| net_avg_win | 59.1837 |
| net_avg_loss | -80.5512 |
| avg_hold_time_bars | 6.9084 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
