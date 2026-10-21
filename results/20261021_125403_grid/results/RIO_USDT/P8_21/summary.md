# EMA Hourly Continuation — RIO/USDT P8_21

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -2.1555 |
| sortino_ratio | -0.6495 |
| max_drawdown | 0.5342 |
| cagr | -0.2590 |
| net_avg_win | 72.9584 |
| net_avg_loss | -85.5327 |
| avg_hold_time_bars | 5.8517 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
