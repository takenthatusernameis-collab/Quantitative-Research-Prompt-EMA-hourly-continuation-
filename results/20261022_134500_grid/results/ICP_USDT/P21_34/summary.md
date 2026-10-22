# EMA Hourly Continuation — ICP/USDT P21_34

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1181 |
| net_profit_factor | 0.3181 |
| net_win_rate | 0.4064 |
| gross_profit_factor | 0.7768 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -11.6096 |
| sortino_ratio | -5.6693 |
| max_drawdown | 0.9994 |
| cagr | -0.9466 |
| net_avg_win | 9.7126 |
| net_avg_loss | -20.9068 |
| avg_hold_time_bars | 2.3946 |
| exposure | 0.1285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
