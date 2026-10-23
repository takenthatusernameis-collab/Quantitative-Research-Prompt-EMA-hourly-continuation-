# EMA Hourly Continuation — BABYDOGE/USDT P8_12

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 14 |
| net_profit_factor | 0.9081 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.1031 |
| sortino_ratio | -0.0055 |
| max_drawdown | 0.0254 |
| cagr | -0.0027 |
| net_avg_win | 96.4228 |
| net_avg_loss | -106.1811 |
| avg_hold_time_bars | 2.4286 |
| exposure | 0.0015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
