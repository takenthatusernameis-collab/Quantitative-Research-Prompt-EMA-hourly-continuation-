# EMA Hourly Continuation — ELON/USDT P20_21

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 116 |
| net_profit_factor | 0.5135 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.7460 |
| gross_win_rate | 0.4224 |
| sharpe_ratio | -2.2864 |
| sortino_ratio | -0.3519 |
| max_drawdown | 0.3560 |
| cagr | -0.1499 |
| net_avg_win | 72.1499 |
| net_avg_loss | -102.7611 |
| avg_hold_time_bars | 7.0517 |
| exposure | 0.0372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
