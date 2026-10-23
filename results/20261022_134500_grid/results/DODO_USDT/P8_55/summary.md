# EMA Hourly Continuation — DODO/USDT P8_55

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1138 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -6.2879 |
| sortino_ratio | -2.9801 |
| max_drawdown | 0.9736 |
| cagr | -0.7572 |
| net_avg_win | 26.5137 |
| net_avg_loss | -37.3123 |
| avg_hold_time_bars | 9.2996 |
| exposure | 0.4789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
