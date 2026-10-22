# EMA Hourly Continuation — KNC/USDT P8_12

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -4.8808 |
| sortino_ratio | -1.6502 |
| max_drawdown | 0.8540 |
| cagr | -0.5328 |
| net_avg_win | 40.3345 |
| net_avg_loss | -65.0953 |
| avg_hold_time_bars | 5.2826 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
