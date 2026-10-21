# EMA Hourly Continuation — NOT/USDT P34_144

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -1.9183 |
| sortino_ratio | -0.4978 |
| max_drawdown | 0.4883 |
| cagr | -0.2052 |
| net_avg_win | 81.3037 |
| net_avg_loss | -94.2007 |
| avg_hold_time_bars | 28.0557 |
| exposure | 0.4257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
