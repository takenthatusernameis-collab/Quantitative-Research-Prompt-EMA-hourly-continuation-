# EMA Hourly Continuation — MANTA/USDT P12_26

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1422 |
| net_profit_factor | 0.5367 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 1.0369 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -9.6823 |
| sortino_ratio | -5.1409 |
| max_drawdown | 0.9983 |
| cagr | -0.9219 |
| net_avg_win | 18.4175 |
| net_avg_loss | -27.1406 |
| avg_hold_time_bars | 3.2729 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
