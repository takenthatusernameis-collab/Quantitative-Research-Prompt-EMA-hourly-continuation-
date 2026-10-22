# EMA Hourly Continuation — JTO/USDT P20_34

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.4973 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.9509 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -8.1577 |
| sortino_ratio | -3.9491 |
| max_drawdown | 0.9922 |
| cagr | -0.8543 |
| net_avg_win | 18.4473 |
| net_avg_loss | -30.7873 |
| avg_hold_time_bars | 2.9744 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
