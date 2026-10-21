# EMA Hourly Continuation — MTL/USDT P21_34

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.5020 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.7562 |
| sortino_ratio | -1.5361 |
| max_drawdown | 0.8487 |
| cagr | -0.5161 |
| net_avg_win | 35.5705 |
| net_avg_loss | -61.3199 |
| avg_hold_time_bars | 5.3626 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
