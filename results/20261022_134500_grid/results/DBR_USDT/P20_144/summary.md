# EMA Hourly Continuation — DBR/USDT P20_144

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.4910 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7736 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -4.3768 |
| sortino_ratio | -1.3674 |
| max_drawdown | 0.7508 |
| cagr | -0.4849 |
| net_avg_win | 40.3314 |
| net_avg_loss | -64.8346 |
| avg_hold_time_bars | 23.3058 |
| exposure | 0.5288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
