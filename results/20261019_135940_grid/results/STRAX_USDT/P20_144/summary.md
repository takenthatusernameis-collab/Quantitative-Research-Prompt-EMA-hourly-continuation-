# EMA Hourly Continuation — STRAX/USDT P20_144

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.5464 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.7853 |
| gross_win_rate | 0.4181 |
| sharpe_ratio | -6.2590 |
| sortino_ratio | -2.3177 |
| max_drawdown | 0.9417 |
| cagr | -0.6776 |
| net_avg_win | 39.7606 |
| net_avg_loss | -50.4611 |
| avg_hold_time_bars | 14.9842 |
| exposure | 0.4768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
