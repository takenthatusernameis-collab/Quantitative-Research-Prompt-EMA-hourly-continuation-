# EMA Hourly Continuation — 1INCH/USDT P55_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.4276 |
| net_win_rate | 0.4281 |
| gross_profit_factor | 0.8072 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -7.2075 |
| sortino_ratio | -2.6081 |
| max_drawdown | 0.9648 |
| cagr | -0.7340 |
| net_avg_win | 25.4436 |
| net_avg_loss | -44.5532 |
| avg_hold_time_bars | 5.1104 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
