# EMA Hourly Continuation — CARV/USDT P50_200

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7891 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -3.4334 |
| sortino_ratio | -0.9145 |
| max_drawdown | 0.5880 |
| cagr | -0.3434 |
| net_avg_win | 52.1814 |
| net_avg_loss | -75.3743 |
| avg_hold_time_bars | 22.4860 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
