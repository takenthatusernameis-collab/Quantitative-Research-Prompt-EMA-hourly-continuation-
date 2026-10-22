# EMA Hourly Continuation — LUNA/USDT P8_89

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.0870 |
| sortino_ratio | -0.6966 |
| max_drawdown | 0.5644 |
| cagr | -0.2755 |
| net_avg_win | 74.3767 |
| net_avg_loss | -89.5669 |
| avg_hold_time_bars | 21.9707 |
| exposure | 0.5463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
