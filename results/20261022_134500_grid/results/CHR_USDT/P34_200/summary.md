# EMA Hourly Continuation — CHR/USDT P34_200

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.8068 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0708 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -1.2767 |
| sortino_ratio | -0.3481 |
| max_drawdown | 0.4058 |
| cagr | -0.1505 |
| net_avg_win | 74.9048 |
| net_avg_loss | -98.6178 |
| avg_hold_time_bars | 33.4877 |
| exposure | 0.5531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
