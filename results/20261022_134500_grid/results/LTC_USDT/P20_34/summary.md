# EMA Hourly Continuation — LTC/USDT P20_34

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.2191 |
| net_win_rate | 0.3757 |
| gross_profit_factor | 0.8535 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -13.6348 |
| sortino_ratio | -6.6869 |
| max_drawdown | 0.9999 |
| cagr | -0.9723 |
| net_avg_win | 6.4958 |
| net_avg_loss | -17.8342 |
| avg_hold_time_bars | 2.2791 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
