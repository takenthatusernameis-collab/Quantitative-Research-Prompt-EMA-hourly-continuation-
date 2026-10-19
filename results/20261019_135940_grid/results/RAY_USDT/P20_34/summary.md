# EMA Hourly Continuation — RAY/USDT P20_34

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1092 |
| net_profit_factor | 0.4876 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -8.8268 |
| sortino_ratio | -4.1208 |
| max_drawdown | 0.9940 |
| cagr | -0.8699 |
| net_avg_win | 20.0390 |
| net_avg_loss | -31.2883 |
| avg_hold_time_bars | 2.9084 |
| exposure | 0.1444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
