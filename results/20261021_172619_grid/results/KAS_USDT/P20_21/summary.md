# EMA Hourly Continuation — KAS/USDT P20_21

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.8710 |
| net_win_rate | 0.5510 |
| gross_profit_factor | 1.2191 |
| gross_win_rate | 0.5510 |
| sharpe_ratio | -0.4090 |
| sortino_ratio | -0.0588 |
| max_drawdown | 0.1534 |
| cagr | -0.0272 |
| net_avg_win | 83.6605 |
| net_avg_loss | -117.8831 |
| avg_hold_time_bars | 4.8673 |
| exposure | 0.0217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
