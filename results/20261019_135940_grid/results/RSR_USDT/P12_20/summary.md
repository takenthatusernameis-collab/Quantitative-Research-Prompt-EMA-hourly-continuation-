# EMA Hourly Continuation — RSR/USDT P12_20

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1463 |
| net_profit_factor | 0.4035 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -11.2968 |
| sortino_ratio | -6.0905 |
| max_drawdown | 0.9996 |
| cagr | -0.9559 |
| net_avg_win | 10.5476 |
| net_avg_loss | -20.3857 |
| avg_hold_time_bars | 2.2454 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
