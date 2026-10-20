# EMA Hourly Continuation — REQ/USDT P8_50

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.3993 |
| net_win_rate | 0.4003 |
| gross_profit_factor | 0.7688 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -10.4469 |
| sortino_ratio | -4.9939 |
| max_drawdown | 0.9983 |
| cagr | -0.9206 |
| net_avg_win | 14.4272 |
| net_avg_loss | -24.1208 |
| avg_hold_time_bars | 9.0688 |
| exposure | 0.4736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
