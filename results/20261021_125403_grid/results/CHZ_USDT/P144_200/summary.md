# EMA Hourly Continuation — CHZ/USDT P144_200

**Symbol:** CHZ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6267 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.0051 |
| sortino_ratio | -0.4011 |
| max_drawdown | 0.3869 |
| cagr | -0.1681 |
| net_avg_win | 68.2641 |
| net_avg_loss | -94.4042 |
| avg_hold_time_bars | 7.4235 |
| exposure | 0.0661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
