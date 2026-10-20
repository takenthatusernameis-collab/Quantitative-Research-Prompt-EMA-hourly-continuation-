# EMA Hourly Continuation — MASK/USDT P8_26

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.3204 |
| net_win_rate | 0.4291 |
| gross_profit_factor | 0.7443 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -10.9573 |
| sortino_ratio | -5.8964 |
| max_drawdown | 0.9995 |
| cagr | -0.9499 |
| net_avg_win | 7.4910 |
| net_avg_loss | -17.5704 |
| avg_hold_time_bars | 4.7503 |
| exposure | 0.3165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
