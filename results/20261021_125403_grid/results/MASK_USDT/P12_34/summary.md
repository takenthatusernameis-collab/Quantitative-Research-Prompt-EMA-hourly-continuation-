# EMA Hourly Continuation — MASK/USDT P12_34

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6427 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -4.0254 |
| sortino_ratio | -1.5195 |
| max_drawdown | 0.8284 |
| cagr | -0.5043 |
| net_avg_win | 44.8811 |
| net_avg_loss | -63.3446 |
| avg_hold_time_bars | 7.6261 |
| exposure | 0.2420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
