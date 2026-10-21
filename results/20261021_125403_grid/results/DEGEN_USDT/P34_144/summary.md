# EMA Hourly Continuation — DEGEN/USDT P34_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.9112 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0613 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -0.5988 |
| sortino_ratio | -0.1628 |
| max_drawdown | 0.3542 |
| cagr | -0.0761 |
| net_avg_win | 100.3536 |
| net_avg_loss | -116.4666 |
| avg_hold_time_bars | 24.6844 |
| exposure | 0.4023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
