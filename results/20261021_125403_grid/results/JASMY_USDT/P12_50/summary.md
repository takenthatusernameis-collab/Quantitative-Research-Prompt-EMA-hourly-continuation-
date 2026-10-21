# EMA Hourly Continuation — JASMY/USDT P12_50

**Symbol:** JASMY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.7852 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.8326 |
| sortino_ratio | -0.6482 |
| max_drawdown | 0.5650 |
| cagr | -0.2587 |
| net_avg_win | 63.5558 |
| net_avg_loss | -80.4126 |
| avg_hold_time_bars | 10.6738 |
| exposure | 0.2960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
