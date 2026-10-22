# EMA Hourly Continuation — XLM/USDT P20_26

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1226 |
| net_profit_factor | 0.1075 |
| net_win_rate | 0.3369 |
| gross_profit_factor | 0.7170 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -16.2189 |
| sortino_ratio | -8.4825 |
| max_drawdown | 1.0000 |
| cagr | -0.9902 |
| net_avg_win | 2.9171 |
| net_avg_loss | -13.7819 |
| avg_hold_time_bars | 1.8891 |
| exposure | 0.1053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
