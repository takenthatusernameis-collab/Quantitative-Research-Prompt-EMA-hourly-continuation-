# EMA Hourly Continuation — BSV/USDT P34_100

**Symbol:** BSV/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.2862 |
| sortino_ratio | -1.0109 |
| max_drawdown | 0.6974 |
| cagr | -0.3710 |
| net_avg_win | 52.8272 |
| net_avg_loss | -71.8726 |
| avg_hold_time_bars | 13.1135 |
| exposure | 0.2784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
