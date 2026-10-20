# EMA Hourly Continuation — MOCA/USDT P50_89

**Symbol:** MOCA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.4673 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8000 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.0767 |
| sortino_ratio | -2.1694 |
| max_drawdown | 0.9164 |
| cagr | -0.6577 |
| net_avg_win | 31.2897 |
| net_avg_loss | -52.2552 |
| avg_hold_time_bars | 4.8579 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
