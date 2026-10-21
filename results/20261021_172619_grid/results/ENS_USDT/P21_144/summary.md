# EMA Hourly Continuation — ENS/USDT P21_144

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7862 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9487 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.3442 |
| sortino_ratio | -0.3597 |
| max_drawdown | 0.4070 |
| cagr | -0.1537 |
| net_avg_win | 73.1878 |
| net_avg_loss | -89.4529 |
| avg_hold_time_bars | 35.1909 |
| exposure | 0.5615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
