# EMA Hourly Continuation — AUCTION/USDT P21_34

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.4669 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.7201 |
| gross_win_rate | 0.4204 |
| sharpe_ratio | -5.3247 |
| sortino_ratio | -1.6110 |
| max_drawdown | 0.8578 |
| cagr | -0.5339 |
| net_avg_win | 39.5823 |
| net_avg_loss | -60.9241 |
| avg_hold_time_bars | 6.3562 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
