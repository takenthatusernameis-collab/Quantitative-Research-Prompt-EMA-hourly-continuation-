# EMA Hourly Continuation — DEGEN/USDT P34_200

**Symbol:** DEGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.8830 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -0.6743 |
| sortino_ratio | -0.1651 |
| max_drawdown | 0.2375 |
| cagr | -0.0760 |
| net_avg_win | 91.7065 |
| net_avg_loss | -106.7451 |
| avg_hold_time_bars | 37.5582 |
| exposure | 0.4993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
