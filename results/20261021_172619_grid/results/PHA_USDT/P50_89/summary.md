# EMA Hourly Continuation — PHA/USDT P50_89

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7191 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.9325 |
| sortino_ratio | -0.5247 |
| max_drawdown | 0.4800 |
| cagr | -0.2139 |
| net_avg_win | 66.7215 |
| net_avg_loss | -86.3403 |
| avg_hold_time_bars | 7.0222 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
