# EMA Hourly Continuation — ATH/USDT P34_89

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6110 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -3.7122 |
| sortino_ratio | -1.4138 |
| max_drawdown | 0.8032 |
| cagr | -0.4910 |
| net_avg_win | 36.5676 |
| net_avg_loss | -59.6734 |
| avg_hold_time_bars | 6.6920 |
| exposure | 0.2222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
