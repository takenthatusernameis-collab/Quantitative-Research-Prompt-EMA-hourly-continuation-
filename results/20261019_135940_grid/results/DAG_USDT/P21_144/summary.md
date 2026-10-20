# EMA Hourly Continuation — DAG/USDT P21_144

**Symbol:** DAG/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.5660 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.7852 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -4.1775 |
| sortino_ratio | -1.4466 |
| max_drawdown | 0.8310 |
| cagr | -0.5026 |
| net_avg_win | 39.6516 |
| net_avg_loss | -55.8783 |
| avg_hold_time_bars | 16.6949 |
| exposure | 0.4652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
