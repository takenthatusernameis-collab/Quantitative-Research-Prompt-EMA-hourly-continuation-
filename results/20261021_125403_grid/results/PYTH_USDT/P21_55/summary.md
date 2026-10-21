# EMA Hourly Continuation — PYTH/USDT P21_55

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.8942 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.4002 |
| sortino_ratio | -0.7547 |
| max_drawdown | 0.5965 |
| cagr | -0.2930 |
| net_avg_win | 63.3649 |
| net_avg_loss | -78.7728 |
| avg_hold_time_bars | 8.7207 |
| exposure | 0.1930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
