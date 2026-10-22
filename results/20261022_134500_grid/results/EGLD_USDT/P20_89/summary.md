# EMA Hourly Continuation — EGLD/USDT P20_89

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.6052 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -4.3046 |
| sortino_ratio | -1.6038 |
| max_drawdown | 0.8682 |
| cagr | -0.5419 |
| net_avg_win | 38.8595 |
| net_avg_loss | -59.1450 |
| avg_hold_time_bars | 12.4356 |
| exposure | 0.3996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
