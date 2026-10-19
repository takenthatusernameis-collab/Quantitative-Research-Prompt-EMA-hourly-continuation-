# EMA Hourly Continuation — MNT/USDT P55_200

**Symbol:** MNT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6493 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9682 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.9084 |
| sortino_ratio | -0.4528 |
| max_drawdown | 0.4836 |
| cagr | -0.1928 |
| net_avg_win | 54.9974 |
| net_avg_loss | -84.1059 |
| avg_hold_time_bars | 33.4270 |
| exposure | 0.4270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
