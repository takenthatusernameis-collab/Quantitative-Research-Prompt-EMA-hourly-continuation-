# EMA Hourly Continuation — AXL/USDT P8_21

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1706 |
| net_profit_factor | 0.4601 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.8639 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -11.6940 |
| sortino_ratio | -6.8057 |
| max_drawdown | 0.9998 |
| cagr | -0.9651 |
| net_avg_win | 12.0679 |
| net_avg_loss | -18.5178 |
| avg_hold_time_bars | 3.3159 |
| exposure | 0.2560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
