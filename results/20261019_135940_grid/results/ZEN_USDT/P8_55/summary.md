# EMA Hourly Continuation — ZEN/USDT P8_55

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1122 |
| net_profit_factor | 0.4923 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.8037 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -7.0057 |
| sortino_ratio | -3.2777 |
| max_drawdown | 0.9826 |
| cagr | -0.7996 |
| net_avg_win | 19.2052 |
| net_avg_loss | -30.9095 |
| avg_hold_time_bars | 9.6043 |
| exposure | 0.4898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
