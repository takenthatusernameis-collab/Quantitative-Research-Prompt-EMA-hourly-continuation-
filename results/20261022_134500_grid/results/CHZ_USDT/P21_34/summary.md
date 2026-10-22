# EMA Hourly Continuation — CHZ/USDT P21_34

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1170 |
| net_profit_factor | 0.3962 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.9167 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -10.8795 |
| sortino_ratio | -5.2978 |
| max_drawdown | 0.9988 |
| cagr | -0.9318 |
| net_avg_win | 13.1599 |
| net_avg_loss | -24.6159 |
| avg_hold_time_bars | 2.4094 |
| exposure | 0.1281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
