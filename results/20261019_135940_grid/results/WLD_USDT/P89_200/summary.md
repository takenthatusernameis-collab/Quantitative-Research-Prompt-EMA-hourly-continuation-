# EMA Hourly Continuation — WLD/USDT P89_200

**Symbol:** WLD/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7418 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.6347 |
| sortino_ratio | -0.4050 |
| max_drawdown | 0.4489 |
| cagr | -0.1711 |
| net_avg_win | 72.4600 |
| net_avg_loss | -95.7587 |
| avg_hold_time_bars | 14.8904 |
| exposure | 0.2037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
