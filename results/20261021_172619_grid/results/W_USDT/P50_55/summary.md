# EMA Hourly Continuation — W/USDT P50_55

**Symbol:** W/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 117 |
| net_profit_factor | 0.7733 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0297 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -0.7971 |
| sortino_ratio | -0.1241 |
| max_drawdown | 0.1692 |
| cagr | -0.0555 |
| net_avg_win | 76.0147 |
| net_avg_loss | -103.4684 |
| avg_hold_time_bars | 4.6581 |
| exposure | 0.0248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
