# EMA Hourly Continuation — CSPR/USDT P34_100

**Symbol:** CSPR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 944 |
| net_profit_factor | 0.4455 |
| net_win_rate | 0.4174 |
| gross_profit_factor | 0.7750 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -7.5526 |
| sortino_ratio | -3.2663 |
| max_drawdown | 0.9825 |
| cagr | -0.7966 |
| net_avg_win | 20.0180 |
| net_avg_loss | -32.1889 |
| avg_hold_time_bars | 6.2267 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
