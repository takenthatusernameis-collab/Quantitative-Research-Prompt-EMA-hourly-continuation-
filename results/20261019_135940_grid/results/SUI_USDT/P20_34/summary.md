# EMA Hourly Continuation — SUI/USDT P20_34

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.4459 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.8625 |
| gross_win_rate | 0.4206 |
| sharpe_ratio | -11.3745 |
| sortino_ratio | -5.5243 |
| max_drawdown | 0.9993 |
| cagr | -0.9429 |
| net_avg_win | 17.1086 |
| net_avg_loss | -25.5071 |
| avg_hold_time_bars | 2.5735 |
| exposure | 0.1377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
