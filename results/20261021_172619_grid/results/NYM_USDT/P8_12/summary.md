# EMA Hourly Continuation — NYM/USDT P8_12

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.2842 |
| net_win_rate | 0.3882 |
| gross_profit_factor | 0.6261 |
| gross_win_rate | 0.4059 |
| sharpe_ratio | -5.7006 |
| sortino_ratio | -1.5109 |
| max_drawdown | 0.8407 |
| cagr | -0.5162 |
| net_avg_win | 25.2193 |
| net_avg_loss | -56.3177 |
| avg_hold_time_bars | 9.6853 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
