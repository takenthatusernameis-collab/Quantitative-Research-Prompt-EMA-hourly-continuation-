# EMA Hourly Continuation — BSV/USDT P34_50

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.5703 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.9218 |
| sortino_ratio | -0.7380 |
| max_drawdown | 0.5690 |
| cagr | -0.2848 |
| net_avg_win | 51.7290 |
| net_avg_loss | -80.7463 |
| avg_hold_time_bars | 6.2065 |
| exposure | 0.0875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
