# EMA Hourly Continuation — VR/USDT P26_55

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.6048 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -3.0258 |
| sortino_ratio | -0.7736 |
| max_drawdown | 0.5993 |
| cagr | -0.3027 |
| net_avg_win | 62.4246 |
| net_avg_loss | -84.1919 |
| avg_hold_time_bars | 9.6800 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
