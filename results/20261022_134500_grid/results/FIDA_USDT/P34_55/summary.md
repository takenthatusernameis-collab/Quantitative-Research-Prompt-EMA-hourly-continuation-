# EMA Hourly Continuation — FIDA/USDT P34_55

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.3744 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.7945 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -8.0700 |
| sortino_ratio | -3.3256 |
| max_drawdown | 0.9848 |
| cagr | -0.8081 |
| net_avg_win | 16.3671 |
| net_avg_loss | -32.0503 |
| avg_hold_time_bars | 4.2045 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
