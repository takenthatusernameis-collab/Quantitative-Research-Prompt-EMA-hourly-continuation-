# EMA Hourly Continuation — SUN/USDT P55_200

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.3845 |
| net_win_rate | 0.3818 |
| gross_profit_factor | 0.7651 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -6.0326 |
| sortino_ratio | -1.5762 |
| max_drawdown | 0.8811 |
| cagr | -0.5675 |
| net_avg_win | 40.9836 |
| net_avg_loss | -65.8282 |
| avg_hold_time_bars | 24.0655 |
| exposure | 0.3823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
