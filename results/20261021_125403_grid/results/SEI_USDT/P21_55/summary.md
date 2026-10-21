# EMA Hourly Continuation — SEI/USDT P21_55

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8001 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0245 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.5790 |
| sortino_ratio | -0.4883 |
| max_drawdown | 0.4767 |
| cagr | -0.2013 |
| net_avg_win | 73.7780 |
| net_avg_loss | -93.8185 |
| avg_hold_time_bars | 8.6013 |
| exposure | 0.1814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
