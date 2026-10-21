# EMA Hourly Continuation — QNT/USDT P26_89

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.7460 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0141 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.9906 |
| sortino_ratio | -0.6699 |
| max_drawdown | 0.5715 |
| cagr | -0.2639 |
| net_avg_win | 56.5024 |
| net_avg_loss | -78.5548 |
| avg_hold_time_bars | 10.3814 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
