# EMA Hourly Continuation — DUSK/USDT P26_34

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6257 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8893 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -2.3829 |
| sortino_ratio | -0.5541 |
| max_drawdown | 0.5147 |
| cagr | -0.2239 |
| net_avg_win | 63.4786 |
| net_avg_loss | -89.8597 |
| avg_hold_time_bars | 4.3788 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
