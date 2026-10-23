# EMA Hourly Continuation — YGG/USDT P21_89

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.6965 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 1.0287 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -3.7978 |
| sortino_ratio | -1.4668 |
| max_drawdown | 0.8370 |
| cagr | -0.5020 |
| net_avg_win | 52.4842 |
| net_avg_loss | -69.7609 |
| avg_hold_time_bars | 10.5020 |
| exposure | 0.3578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
