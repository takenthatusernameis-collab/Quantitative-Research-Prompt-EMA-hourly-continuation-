# EMA Hourly Continuation — EDU/USDT P50_144

**Symbol:** EDU/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.6033 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.5212 |
| sortino_ratio | -1.1807 |
| max_drawdown | 0.7648 |
| cagr | -0.4266 |
| net_avg_win | 43.2744 |
| net_avg_loss | -63.5761 |
| avg_hold_time_bars | 10.6649 |
| exposure | 0.2722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
