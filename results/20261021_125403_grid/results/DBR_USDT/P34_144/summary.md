# EMA Hourly Continuation — DBR/USDT P34_144

**Symbol:** DBR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.6806 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9052 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.1360 |
| sortino_ratio | -0.5628 |
| max_drawdown | 0.4293 |
| cagr | -0.2276 |
| net_avg_win | 65.7894 |
| net_avg_loss | -89.1782 |
| avg_hold_time_bars | 23.5458 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
