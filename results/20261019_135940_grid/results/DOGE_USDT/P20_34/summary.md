# EMA Hourly Continuation — DOGE/USDT P20_34

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.3061 |
| net_win_rate | 0.4013 |
| gross_profit_factor | 0.7716 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -11.6871 |
| sortino_ratio | -5.5645 |
| max_drawdown | 0.9993 |
| cagr | -0.9456 |
| net_avg_win | 9.8175 |
| net_avg_loss | -21.4945 |
| avg_hold_time_bars | 2.6032 |
| exposure | 0.1324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
