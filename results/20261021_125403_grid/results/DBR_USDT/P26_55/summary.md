# EMA Hourly Continuation — DBR/USDT P26_55

**Symbol:** DBR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.5571 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8465 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -3.8219 |
| sortino_ratio | -1.0982 |
| max_drawdown | 0.6544 |
| cagr | -0.3992 |
| net_avg_win | 54.7872 |
| net_avg_loss | -80.7683 |
| avg_hold_time_bars | 10.0736 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
