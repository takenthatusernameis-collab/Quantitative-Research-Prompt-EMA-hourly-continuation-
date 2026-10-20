# EMA Hourly Continuation — POKT/USDT P20_55

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.4803 |
| net_win_rate | 0.3987 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -9.1883 |
| sortino_ratio | -4.2762 |
| max_drawdown | 0.9954 |
| cagr | -0.8804 |
| net_avg_win | 20.7635 |
| net_avg_loss | -28.6692 |
| avg_hold_time_bars | 5.2709 |
| exposure | 0.2650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
