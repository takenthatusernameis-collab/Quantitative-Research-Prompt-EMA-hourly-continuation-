# EMA Hourly Continuation — VET/USDT P20_34

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7263 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0585 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.7926 |
| sortino_ratio | -0.4682 |
| max_drawdown | 0.4337 |
| cagr | -0.1919 |
| net_avg_win | 65.0911 |
| net_avg_loss | -95.2513 |
| avg_hold_time_bars | 5.1921 |
| exposure | 0.0774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
