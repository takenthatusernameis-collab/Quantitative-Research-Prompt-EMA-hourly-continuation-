# EMA Hourly Continuation — CTC/USDT P8_21

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1610 |
| net_profit_factor | 0.3237 |
| net_win_rate | 0.4186 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -12.3847 |
| sortino_ratio | -7.0250 |
| max_drawdown | 0.9999 |
| cagr | -0.9716 |
| net_avg_win | 7.1008 |
| net_avg_loss | -15.7955 |
| avg_hold_time_bars | 3.6826 |
| exposure | 0.2695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
