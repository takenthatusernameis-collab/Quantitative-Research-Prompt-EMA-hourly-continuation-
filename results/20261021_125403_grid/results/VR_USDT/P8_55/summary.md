# EMA Hourly Continuation — VR/USDT P8_55

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.7841 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9682 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.8792 |
| sortino_ratio | -0.6314 |
| max_drawdown | 0.5255 |
| cagr | -0.2542 |
| net_avg_win | 69.3220 |
| net_avg_loss | -85.5928 |
| avg_hold_time_bars | 17.3964 |
| exposure | 0.4389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
