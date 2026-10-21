# EMA Hourly Continuation — AR/USDT P8_34

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.7339 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9209 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -2.6593 |
| sortino_ratio | -1.0184 |
| max_drawdown | 0.7054 |
| cagr | -0.3740 |
| net_avg_win | 54.9712 |
| net_avg_loss | -69.6802 |
| avg_hold_time_bars | 9.2139 |
| exposure | 0.3015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
