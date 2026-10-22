# EMA Hourly Continuation — MANTA/USDT P26_55

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6678 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8779 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.1251 |
| sortino_ratio | -0.9761 |
| max_drawdown | 0.6854 |
| cagr | -0.3619 |
| net_avg_win | 61.5180 |
| net_avg_loss | -78.3045 |
| avg_hold_time_bars | 6.8482 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
