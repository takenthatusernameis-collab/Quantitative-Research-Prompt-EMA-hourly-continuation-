# EMA Hourly Continuation — ZETA/USDT P55_200

**Symbol:** ZETA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7817 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9495 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.3247 |
| sortino_ratio | -0.3153 |
| max_drawdown | 0.3853 |
| cagr | -0.1364 |
| net_avg_win | 81.4157 |
| net_avg_loss | -98.3660 |
| avg_hold_time_bars | 32.4250 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
