# EMA Hourly Continuation — NYM/USDT P12_34

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1118 |
| net_profit_factor | 0.2496 |
| net_win_rate | 0.3497 |
| gross_profit_factor | 0.6742 |
| gross_win_rate | 0.3873 |
| sharpe_ratio | -14.3306 |
| sortino_ratio | -6.9233 |
| max_drawdown | 0.9999 |
| cagr | -0.9779 |
| net_avg_win | 8.5046 |
| net_avg_loss | -18.3282 |
| avg_hold_time_bars | 6.1655 |
| exposure | 0.3133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
