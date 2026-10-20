# EMA Hourly Continuation — GMT/USDT P12_34

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1323 |
| net_profit_factor | 0.4296 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8444 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -9.4543 |
| sortino_ratio | -4.8427 |
| max_drawdown | 0.9977 |
| cagr | -0.9100 |
| net_avg_win | 12.9083 |
| net_avg_loss | -23.6019 |
| avg_hold_time_bars | 4.1036 |
| exposure | 0.2468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
