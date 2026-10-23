# EMA Hourly Continuation — YGG/USDT P20_21

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.1810 |
| net_win_rate | 0.3145 |
| gross_profit_factor | 0.6176 |
| gross_win_rate | 0.3897 |
| sharpe_ratio | -16.8058 |
| sortino_ratio | -8.7183 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 5.6815 |
| net_avg_loss | -14.3987 |
| avg_hold_time_bars | 1.6928 |
| exposure | 0.0948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
