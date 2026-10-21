# EMA Hourly Continuation — EDU/USDT P12_20

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6862 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.5076 |
| sortino_ratio | -0.7726 |
| max_drawdown | 0.6051 |
| cagr | -0.2984 |
| net_avg_win | 56.6681 |
| net_avg_loss | -79.7876 |
| avg_hold_time_bars | 5.3621 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
