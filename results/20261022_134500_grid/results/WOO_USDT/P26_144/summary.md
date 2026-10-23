# EMA Hourly Continuation — WOO/USDT P26_144

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.7680 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0466 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -2.0525 |
| sortino_ratio | -0.6259 |
| max_drawdown | 0.5959 |
| cagr | -0.2540 |
| net_avg_win | 74.3302 |
| net_avg_loss | -97.2025 |
| avg_hold_time_bars | 23.2095 |
| exposure | 0.4885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
