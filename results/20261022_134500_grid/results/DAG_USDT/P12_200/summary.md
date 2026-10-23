# EMA Hourly Continuation — DAG/USDT P12_200

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6483 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -2.9624 |
| sortino_ratio | -0.9625 |
| max_drawdown | 0.7027 |
| cagr | -0.3645 |
| net_avg_win | 50.1120 |
| net_avg_loss | -69.0198 |
| avg_hold_time_bars | 26.7019 |
| exposure | 0.6433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
