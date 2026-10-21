# EMA Hourly Continuation — COMP/USDT P26_200

**Symbol:** COMP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7215 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -1.7189 |
| sortino_ratio | -0.4580 |
| max_drawdown | 0.4514 |
| cagr | -0.1901 |
| net_avg_win | 63.4187 |
| net_avg_loss | -81.5812 |
| avg_hold_time_bars | 35.6332 |
| exposure | 0.5653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
