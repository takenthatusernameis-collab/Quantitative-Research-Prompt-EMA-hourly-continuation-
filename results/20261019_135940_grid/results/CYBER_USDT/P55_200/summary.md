# EMA Hourly Continuation — CYBER/USDT P55_200

**Symbol:** CYBER/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -2.1659 |
| sortino_ratio | -0.5785 |
| max_drawdown | 0.5310 |
| cagr | -0.2403 |
| net_avg_win | 55.2436 |
| net_avg_loss | -80.3725 |
| avg_hold_time_bars | 23.7465 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
