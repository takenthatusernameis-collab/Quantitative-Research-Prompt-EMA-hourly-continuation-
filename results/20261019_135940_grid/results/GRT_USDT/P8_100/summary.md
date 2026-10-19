# EMA Hourly Continuation — GRT/USDT P8_100

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6832 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9949 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -3.3885 |
| sortino_ratio | -1.2154 |
| max_drawdown | 0.7794 |
| cagr | -0.4422 |
| net_avg_win | 51.9279 |
| net_avg_loss | -73.0436 |
| avg_hold_time_bars | 22.5865 |
| exposure | 0.6674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
