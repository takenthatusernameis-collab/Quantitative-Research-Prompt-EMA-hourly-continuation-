# EMA Hourly Continuation — ORDI/USDT P20_144

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6028 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8070 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -3.8605 |
| sortino_ratio | -1.2724 |
| max_drawdown | 0.7815 |
| cagr | -0.4496 |
| net_avg_win | 48.7019 |
| net_avg_loss | -64.3198 |
| avg_hold_time_bars | 20.1355 |
| exposure | 0.4997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
