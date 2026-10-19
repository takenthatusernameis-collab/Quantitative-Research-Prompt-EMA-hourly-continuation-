# EMA Hourly Continuation — XLM/USDT P12_20

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1593 |
| net_profit_factor | 0.0873 |
| net_win_rate | 0.3578 |
| gross_profit_factor | 0.5224 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -17.0986 |
| sortino_ratio | -9.9315 |
| max_drawdown | 1.0000 |
| cagr | -0.9952 |
| net_avg_win | 1.6781 |
| net_avg_loss | -10.7102 |
| avg_hold_time_bars | 2.0942 |
| exposure | 0.1516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
