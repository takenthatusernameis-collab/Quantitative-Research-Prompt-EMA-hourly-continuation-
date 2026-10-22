# EMA Hourly Continuation — DOGE/USDT P8_21

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1657 |
| net_profit_factor | 0.3512 |
| net_win_rate | 0.4273 |
| gross_profit_factor | 0.8779 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -13.2173 |
| sortino_ratio | -7.5778 |
| max_drawdown | 1.0000 |
| cagr | -0.9813 |
| net_avg_win | 7.6452 |
| net_avg_loss | -16.2406 |
| avg_hold_time_bars | 2.7423 |
| exposure | 0.2065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
