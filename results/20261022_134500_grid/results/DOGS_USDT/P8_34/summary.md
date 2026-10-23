# EMA Hourly Continuation — DOGS/USDT P8_34

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1238 |
| net_profit_factor | 0.5276 |
| net_win_rate | 0.4362 |
| gross_profit_factor | 0.8316 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -8.7060 |
| sortino_ratio | -4.6424 |
| max_drawdown | 0.9925 |
| cagr | -0.8974 |
| net_avg_win | 20.5284 |
| net_avg_loss | -30.1014 |
| avg_hold_time_bars | 4.9717 |
| exposure | 0.3265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
