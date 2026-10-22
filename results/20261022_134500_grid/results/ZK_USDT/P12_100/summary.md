# EMA Hourly Continuation — ZK/USDT P12_100

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.6984 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9779 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -3.2540 |
| sortino_ratio | -1.2132 |
| max_drawdown | 0.7432 |
| cagr | -0.4336 |
| net_avg_win | 55.3260 |
| net_avg_loss | -72.3979 |
| avg_hold_time_bars | 18.5473 |
| exposure | 0.5832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
