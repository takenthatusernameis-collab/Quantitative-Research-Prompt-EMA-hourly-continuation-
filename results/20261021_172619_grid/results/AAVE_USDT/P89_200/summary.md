# EMA Hourly Continuation — AAVE/USDT P89_200

**Symbol:** AAVE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7301 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -1.5409 |
| sortino_ratio | -0.3565 |
| max_drawdown | 0.3460 |
| cagr | -0.1510 |
| net_avg_win | 72.3711 |
| net_avg_loss | -91.1620 |
| avg_hold_time_bars | 15.2662 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
