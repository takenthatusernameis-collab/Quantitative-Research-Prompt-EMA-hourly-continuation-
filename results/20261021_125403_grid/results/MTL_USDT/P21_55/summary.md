# EMA Hourly Continuation — MTL/USDT P21_55

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9749 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -3.2539 |
| sortino_ratio | -1.0963 |
| max_drawdown | 0.7370 |
| cagr | -0.3962 |
| net_avg_win | 56.8119 |
| net_avg_loss | -77.8621 |
| avg_hold_time_bars | 11.1673 |
| exposure | 0.2810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
