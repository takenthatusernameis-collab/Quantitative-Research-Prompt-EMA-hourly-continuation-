# EMA Hourly Continuation — DAG/USDT P26_89

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.4928 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.7662 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -6.5313 |
| sortino_ratio | -2.5355 |
| max_drawdown | 0.9596 |
| cagr | -0.7173 |
| net_avg_win | 28.9086 |
| net_avg_loss | -41.6992 |
| avg_hold_time_bars | 7.5845 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
