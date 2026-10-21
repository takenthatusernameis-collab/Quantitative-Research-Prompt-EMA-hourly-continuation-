# EMA Hourly Continuation — RLC/USDT P20_50

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7037 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9703 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -2.7938 |
| sortino_ratio | -0.9522 |
| max_drawdown | 0.6789 |
| cagr | -0.3536 |
| net_avg_win | 56.8744 |
| net_avg_loss | -77.7461 |
| avg_hold_time_bars | 7.1129 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
