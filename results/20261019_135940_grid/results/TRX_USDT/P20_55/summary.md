# EMA Hourly Continuation — TRX/USDT P20_55

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.2252 |
| net_win_rate | 0.3771 |
| gross_profit_factor | 0.8556 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -12.2165 |
| sortino_ratio | -5.1137 |
| max_drawdown | 0.9992 |
| cagr | -0.9403 |
| net_avg_win | 9.4608 |
| net_avg_loss | -25.4359 |
| avg_hold_time_bars | 5.8600 |
| exposure | 0.2168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
