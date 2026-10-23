# EMA Hourly Continuation — ZRX/USDT P144_200

**Symbol:** ZRX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.4922 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9728 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -4.3948 |
| sortino_ratio | -1.2847 |
| max_drawdown | 0.7952 |
| cagr | -0.4619 |
| net_avg_win | 38.4256 |
| net_avg_loss | -69.9872 |
| avg_hold_time_bars | 4.3017 |
| exposure | 0.0823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
