# EMA Hourly Continuation — ARKM/USDT P144_200

**Symbol:** ARKM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.4716 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.7622 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -4.8468 |
| sortino_ratio | -1.4401 |
| max_drawdown | 0.8267 |
| cagr | -0.5024 |
| net_avg_win | 38.4247 |
| net_avg_loss | -61.5929 |
| avg_hold_time_bars | 4.5717 |
| exposure | 0.0927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
