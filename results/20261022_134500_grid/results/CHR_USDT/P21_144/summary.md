# EMA Hourly Continuation — CHR/USDT P21_144

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7295 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9713 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.2034 |
| sortino_ratio | -0.6629 |
| max_drawdown | 0.5819 |
| cagr | -0.2691 |
| net_avg_win | 66.3665 |
| net_avg_loss | -86.6855 |
| avg_hold_time_bars | 28.3253 |
| exposure | 0.5832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
