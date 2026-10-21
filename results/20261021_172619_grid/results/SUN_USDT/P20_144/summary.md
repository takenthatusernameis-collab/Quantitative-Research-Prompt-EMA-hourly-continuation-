# EMA Hourly Continuation — SUN/USDT P20_144

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.5101 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.7890 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -4.3739 |
| sortino_ratio | -1.1732 |
| max_drawdown | 0.7560 |
| cagr | -0.4261 |
| net_avg_win | 53.3862 |
| net_avg_loss | -72.5648 |
| avg_hold_time_bars | 34.3370 |
| exposure | 0.5578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
