# EMA Hourly Continuation — PEOPLE/USDT P8_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8312 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9564 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.1171 |
| sortino_ratio | -0.2968 |
| max_drawdown | 0.3404 |
| cagr | -0.1293 |
| net_avg_win | 85.3458 |
| net_avg_loss | -97.5193 |
| avg_hold_time_bars | 47.5158 |
| exposure | 0.7504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
