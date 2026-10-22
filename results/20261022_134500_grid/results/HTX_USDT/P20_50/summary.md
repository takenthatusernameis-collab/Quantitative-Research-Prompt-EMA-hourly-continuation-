# EMA Hourly Continuation — HTX/USDT P20_50

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.1835 |
| net_win_rate | 0.2956 |
| gross_profit_factor | 0.6000 |
| gross_win_rate | 0.3604 |
| sharpe_ratio | -16.5284 |
| sortino_ratio | -8.2068 |
| max_drawdown | 1.0000 |
| cagr | -0.9890 |
| net_avg_win | 6.9373 |
| net_avg_loss | -15.8647 |
| avg_hold_time_bars | 5.5484 |
| exposure | 0.2752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
