# EMA Hourly Continuation — CETUS/USDT P12_100

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.8915 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0671 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.7820 |
| sortino_ratio | -0.2484 |
| max_drawdown | 0.3184 |
| cagr | -0.1127 |
| net_avg_win | 84.1815 |
| net_avg_loss | -101.2057 |
| avg_hold_time_bars | 26.4705 |
| exposure | 0.5882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
