# EMA Hourly Continuation — SYN/USDT P8_89

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.8707 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0305 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.0310 |
| sortino_ratio | -0.3359 |
| max_drawdown | 0.4117 |
| cagr | -0.1470 |
| net_avg_win | 84.6252 |
| net_avg_loss | -99.8563 |
| avg_hold_time_bars | 26.3540 |
| exposure | 0.6193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
