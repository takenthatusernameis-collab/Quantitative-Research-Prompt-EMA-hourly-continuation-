# EMA Hourly Continuation — EWT/USDT P21_26

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.2289 |
| net_win_rate | 0.2948 |
| gross_profit_factor | 0.5960 |
| gross_win_rate | 0.3362 |
| sharpe_ratio | -15.7871 |
| sortino_ratio | -7.5600 |
| max_drawdown | 1.0000 |
| cagr | -0.9852 |
| net_avg_win | 9.6991 |
| net_avg_loss | -17.7154 |
| avg_hold_time_bars | 2.4701 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
