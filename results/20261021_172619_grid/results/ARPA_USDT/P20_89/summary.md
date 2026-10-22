# EMA Hourly Continuation — ARPA/USDT P20_89

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6886 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.0285 |
| sortino_ratio | -1.0403 |
| max_drawdown | 0.7299 |
| cagr | -0.3801 |
| net_avg_win | 56.3517 |
| net_avg_loss | -73.0641 |
| avg_hold_time_bars | 13.5386 |
| exposure | 0.3572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
