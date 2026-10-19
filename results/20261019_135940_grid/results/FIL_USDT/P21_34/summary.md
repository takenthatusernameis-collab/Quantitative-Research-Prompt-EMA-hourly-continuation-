# EMA Hourly Continuation — FIL/USDT P21_34

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1143 |
| net_profit_factor | 0.3032 |
| net_win_rate | 0.3963 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -11.6460 |
| sortino_ratio | -5.6270 |
| max_drawdown | 0.9993 |
| cagr | -0.9440 |
| net_avg_win | 9.6001 |
| net_avg_loss | -20.7850 |
| avg_hold_time_bars | 2.3718 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
