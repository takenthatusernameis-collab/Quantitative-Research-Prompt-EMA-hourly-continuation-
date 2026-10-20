# EMA Hourly Continuation — MANTA/USDT P12_55

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 997 |
| net_profit_factor | 0.6094 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -5.9954 |
| sortino_ratio | -2.6543 |
| max_drawdown | 0.9619 |
| cagr | -0.7239 |
| net_avg_win | 33.0758 |
| net_avg_loss | -45.1998 |
| avg_hold_time_bars | 9.4002 |
| exposure | 0.4260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
