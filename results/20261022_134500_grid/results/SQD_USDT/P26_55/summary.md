# EMA Hourly Continuation — SQD/USDT P26_55

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 840 |
| net_profit_factor | 0.6415 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -4.8516 |
| sortino_ratio | -2.0151 |
| max_drawdown | 0.9070 |
| cagr | -0.6183 |
| net_avg_win | 40.6156 |
| net_avg_loss | -57.0150 |
| avg_hold_time_bars | 4.7071 |
| exposure | 0.1859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
