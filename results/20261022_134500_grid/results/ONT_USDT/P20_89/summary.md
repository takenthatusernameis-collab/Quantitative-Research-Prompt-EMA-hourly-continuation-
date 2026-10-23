# EMA Hourly Continuation — ONT/USDT P20_89

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6506 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9662 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -3.8588 |
| sortino_ratio | -1.4248 |
| max_drawdown | 0.8273 |
| cagr | -0.4914 |
| net_avg_win | 46.4573 |
| net_avg_loss | -65.0597 |
| avg_hold_time_bars | 12.4855 |
| exposure | 0.3887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
