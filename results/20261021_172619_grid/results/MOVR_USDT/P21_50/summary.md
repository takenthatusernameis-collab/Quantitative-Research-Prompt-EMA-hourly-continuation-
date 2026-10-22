# EMA Hourly Continuation — MOVR/USDT P21_50

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.5284 |
| sortino_ratio | -0.8411 |
| max_drawdown | 0.6777 |
| cagr | -0.3197 |
| net_avg_win | 60.9250 |
| net_avg_loss | -79.4341 |
| avg_hold_time_bars | 7.2181 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
