# EMA Hourly Continuation — HTX/USDT P12_144

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6268 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.6331 |
| sortino_ratio | -1.0046 |
| max_drawdown | 0.7382 |
| cagr | -0.3776 |
| net_avg_win | 66.5594 |
| net_avg_loss | -93.4525 |
| avg_hold_time_bars | 38.9202 |
| exposure | 0.6622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
