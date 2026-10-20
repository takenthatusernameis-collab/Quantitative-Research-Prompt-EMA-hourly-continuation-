# EMA Hourly Continuation — ONT/USDT P34_89

**Symbol:** ONT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5057 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8050 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -5.4010 |
| sortino_ratio | -1.9766 |
| max_drawdown | 0.9142 |
| cagr | -0.6154 |
| net_avg_win | 30.6296 |
| net_avg_loss | -48.5842 |
| avg_hold_time_bars | 8.2577 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
