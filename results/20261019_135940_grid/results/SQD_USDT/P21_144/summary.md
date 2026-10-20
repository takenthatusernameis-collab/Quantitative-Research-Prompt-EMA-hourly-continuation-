# EMA Hourly Continuation — SQD/USDT P21_144

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7889 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.7345 |
| sortino_ratio | -0.5709 |
| max_drawdown | 0.5222 |
| cagr | -0.2352 |
| net_avg_win | 69.0572 |
| net_avg_loss | -87.5328 |
| avg_hold_time_bars | 20.2819 |
| exposure | 0.4938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
