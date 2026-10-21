# EMA Hourly Continuation — ORDI/USDT P89_200

**Symbol:** ORDI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6856 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8393 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -1.7765 |
| sortino_ratio | -0.4142 |
| max_drawdown | 0.3976 |
| cagr | -0.1738 |
| net_avg_win | 66.4344 |
| net_avg_loss | -84.1172 |
| avg_hold_time_bars | 15.8662 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
