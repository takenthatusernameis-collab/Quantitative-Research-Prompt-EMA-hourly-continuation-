# EMA Hourly Continuation — WLD/USDT P8_34

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.9034 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1184 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.7678 |
| sortino_ratio | -0.2917 |
| max_drawdown | 0.4414 |
| cagr | -0.1317 |
| net_avg_win | 75.9052 |
| net_avg_loss | -95.1361 |
| avg_hold_time_bars | 8.5786 |
| exposure | 0.2702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
