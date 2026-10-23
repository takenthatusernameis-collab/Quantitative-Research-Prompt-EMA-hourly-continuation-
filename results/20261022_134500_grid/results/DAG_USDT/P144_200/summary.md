# EMA Hourly Continuation — DAG/USDT P144_200

**Symbol:** DAG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.4443 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.7422 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -4.8852 |
| sortino_ratio | -1.3595 |
| max_drawdown | 0.8211 |
| cagr | -0.4961 |
| net_avg_win | 38.6122 |
| net_avg_loss | -64.8039 |
| avg_hold_time_bars | 4.6332 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
