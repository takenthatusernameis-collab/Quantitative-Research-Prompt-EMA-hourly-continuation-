# EMA Hourly Continuation — CFG/USDT P12_34

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.3808 |
| net_win_rate | 0.4200 |
| gross_profit_factor | 0.6861 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -7.8370 |
| sortino_ratio | -3.5182 |
| max_drawdown | 0.9869 |
| cagr | -0.8202 |
| net_avg_win | 14.1726 |
| net_avg_loss | -26.9567 |
| avg_hold_time_bars | 9.3435 |
| exposure | 0.4328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
