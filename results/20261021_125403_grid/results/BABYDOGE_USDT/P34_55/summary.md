# EMA Hourly Continuation — BABYDOGE/USDT P34_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 18 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7920 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -0.4421 |
| sortino_ratio | -0.0264 |
| max_drawdown | 0.0426 |
| cagr | -0.0122 |
| net_avg_win | 92.7853 |
| net_avg_loss | -104.6107 |
| avg_hold_time_bars | 5.9444 |
| exposure | 0.0048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
