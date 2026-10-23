# EMA Hourly Continuation — FIDA/USDT P8_50

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.5515 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -5.6424 |
| sortino_ratio | -2.5777 |
| max_drawdown | 0.9568 |
| cagr | -0.7100 |
| net_avg_win | 23.7488 |
| net_avg_loss | -37.6597 |
| avg_hold_time_bars | 10.0924 |
| exposure | 0.4845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
