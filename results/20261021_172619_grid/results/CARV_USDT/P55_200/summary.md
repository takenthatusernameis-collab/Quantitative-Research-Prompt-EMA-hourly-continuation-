# EMA Hourly Continuation — CARV/USDT P55_200

**Symbol:** CARV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -1.7037 |
| sortino_ratio | -0.3850 |
| max_drawdown | 0.3180 |
| cagr | -0.1611 |
| net_avg_win | 71.9696 |
| net_avg_loss | -90.2315 |
| avg_hold_time_bars | 29.0588 |
| exposure | 0.3336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
