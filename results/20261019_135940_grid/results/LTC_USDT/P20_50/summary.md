# EMA Hourly Continuation — LTC/USDT P20_50

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.3050 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.8178 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -9.7932 |
| sortino_ratio | -4.4053 |
| max_drawdown | 0.9968 |
| cagr | -0.8972 |
| net_avg_win | 9.9163 |
| net_avg_loss | -24.9826 |
| avg_hold_time_bars | 4.1074 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
