# EMA Hourly Continuation — DAG/USDT P12_89

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.4878 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7437 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -6.5368 |
| sortino_ratio | -2.6596 |
| max_drawdown | 0.9671 |
| cagr | -0.7399 |
| net_avg_win | 25.0021 |
| net_avg_loss | -37.8736 |
| avg_hold_time_bars | 11.5739 |
| exposure | 0.4556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
