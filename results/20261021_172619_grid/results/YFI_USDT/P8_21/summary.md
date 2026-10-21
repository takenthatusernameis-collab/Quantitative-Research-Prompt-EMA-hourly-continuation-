# EMA Hourly Continuation — YFI/USDT P8_21

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.4675 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.7864 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -5.7184 |
| sortino_ratio | -2.1977 |
| max_drawdown | 0.9235 |
| cagr | -0.6366 |
| net_avg_win | 24.7578 |
| net_avg_loss | -44.2907 |
| avg_hold_time_bars | 5.7228 |
| exposure | 0.1859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
