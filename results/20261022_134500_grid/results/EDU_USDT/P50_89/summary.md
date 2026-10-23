# EMA Hourly Continuation — EDU/USDT P50_89

**Symbol:** EDU/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -5.4676 |
| sortino_ratio | -2.0407 |
| max_drawdown | 0.9165 |
| cagr | -0.6209 |
| net_avg_win | 30.0410 |
| net_avg_loss | -48.2429 |
| avg_hold_time_bars | 5.0130 |
| exposure | 0.1574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
