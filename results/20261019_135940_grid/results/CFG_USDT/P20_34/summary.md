# EMA Hourly Continuation — CFG/USDT P20_34

**Symbol:** CFG/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.2839 |
| net_win_rate | 0.3905 |
| gross_profit_factor | 0.6483 |
| gross_win_rate | 0.4086 |
| sharpe_ratio | -9.3635 |
| sortino_ratio | -3.9159 |
| max_drawdown | 0.9933 |
| cagr | -0.8622 |
| net_avg_win | 11.4447 |
| net_avg_loss | -25.8249 |
| avg_hold_time_bars | 9.0965 |
| exposure | 0.3643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
