# EMA Hourly Continuation — ANKR/USDT P34_55

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5832 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8771 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -4.0302 |
| sortino_ratio | -1.1572 |
| max_drawdown | 0.7425 |
| cagr | -0.4153 |
| net_avg_win | 57.5421 |
| net_avg_loss | -79.6381 |
| avg_hold_time_bars | 8.5261 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
