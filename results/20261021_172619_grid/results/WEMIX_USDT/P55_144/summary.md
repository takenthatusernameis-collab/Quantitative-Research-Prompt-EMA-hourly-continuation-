# EMA Hourly Continuation — WEMIX/USDT P55_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6439 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8341 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -2.7766 |
| sortino_ratio | -0.7472 |
| max_drawdown | 0.5822 |
| cagr | -0.2914 |
| net_avg_win | 64.6323 |
| net_avg_loss | -82.5393 |
| avg_hold_time_bars | 15.6964 |
| exposure | 0.2561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
