# EMA Hourly Continuation — BDX/USDT P21_200

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.3807 |
| net_win_rate | 0.3442 |
| gross_profit_factor | 0.7622 |
| gross_win_rate | 0.3823 |
| sharpe_ratio | -12.4680 |
| sortino_ratio | -5.5116 |
| max_drawdown | 0.9995 |
| cagr | -0.9482 |
| net_avg_win | 18.8490 |
| net_avg_loss | -25.9885 |
| avg_hold_time_bars | 10.3168 |
| exposure | 0.4441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
