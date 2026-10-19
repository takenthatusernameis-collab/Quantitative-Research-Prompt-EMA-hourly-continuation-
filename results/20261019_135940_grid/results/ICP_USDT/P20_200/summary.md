# EMA Hourly Continuation — ICP/USDT P20_200

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5699 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -3.4877 |
| sortino_ratio | -0.9631 |
| max_drawdown | 0.7142 |
| cagr | -0.3819 |
| net_avg_win | 51.0576 |
| net_avg_loss | -75.8400 |
| avg_hold_time_bars | 35.6474 |
| exposure | 0.6433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
