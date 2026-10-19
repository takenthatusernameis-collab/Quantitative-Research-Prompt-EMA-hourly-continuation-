# EMA Hourly Continuation — NEO/USDT P20_100

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.5309 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8479 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.9092 |
| sortino_ratio | -1.7313 |
| max_drawdown | 0.8796 |
| cagr | -0.5640 |
| net_avg_win | 35.0151 |
| net_avg_loss | -54.1028 |
| avg_hold_time_bars | 15.8567 |
| exposure | 0.4526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
