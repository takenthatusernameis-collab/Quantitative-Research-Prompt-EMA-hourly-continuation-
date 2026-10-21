# EMA Hourly Continuation — LTC/USDT P12_26

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7060 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.1149 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -2.2460 |
| sortino_ratio | -0.6203 |
| max_drawdown | 0.5203 |
| cagr | -0.2446 |
| net_avg_win | 63.8980 |
| net_avg_loss | -98.2660 |
| avg_hold_time_bars | 5.4192 |
| exposure | 0.0899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
