# EMA Hourly Continuation — SKY/USDT P20_21

**Symbol:** SKY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.1630 |
| net_win_rate | 0.3067 |
| gross_profit_factor | 0.6822 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -17.4046 |
| sortino_ratio | -9.1035 |
| max_drawdown | 1.0000 |
| cagr | -0.9939 |
| net_avg_win | 6.5127 |
| net_avg_loss | -17.6731 |
| avg_hold_time_bars | 1.9190 |
| exposure | 0.1043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
