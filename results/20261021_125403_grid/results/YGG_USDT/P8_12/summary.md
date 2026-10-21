# EMA Hourly Continuation — YGG/USDT P8_12

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -2.0436 |
| sortino_ratio | -0.5487 |
| max_drawdown | 0.4955 |
| cagr | -0.2226 |
| net_avg_win | 66.7129 |
| net_avg_loss | -94.8814 |
| avg_hold_time_bars | 4.3732 |
| exposure | 0.0695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
