# EMA Hourly Continuation — ELON/USDT P12_100

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.5496 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8315 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -5.0968 |
| sortino_ratio | -1.9962 |
| max_drawdown | 0.9099 |
| cagr | -0.6132 |
| net_avg_win | 31.3023 |
| net_avg_loss | -48.0009 |
| avg_hold_time_bars | 14.6822 |
| exposure | 0.5165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
