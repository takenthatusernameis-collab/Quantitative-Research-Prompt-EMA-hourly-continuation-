# EMA Hourly Continuation — ACE/USDT P20_200

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.8661 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -0.7347 |
| sortino_ratio | -0.1904 |
| max_drawdown | 0.3130 |
| cagr | -0.0864 |
| net_avg_win | 78.4367 |
| net_avg_loss | -94.5038 |
| avg_hold_time_bars | 41.0851 |
| exposure | 0.6117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
