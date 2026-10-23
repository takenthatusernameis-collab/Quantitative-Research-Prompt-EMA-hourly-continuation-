# EMA Hourly Continuation — FLUX/USDT P144_200

**Symbol:** FLUX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.4971 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8963 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.9248 |
| sortino_ratio | -1.0743 |
| max_drawdown | 0.7400 |
| cagr | -0.4024 |
| net_avg_win | 40.7450 |
| net_avg_loss | -73.6034 |
| avg_hold_time_bars | 4.8280 |
| exposure | 0.0816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
