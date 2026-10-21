# EMA Hourly Continuation — MAGIC/USDT P34_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9453 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.6317 |
| sortino_ratio | -0.4168 |
| max_drawdown | 0.4129 |
| cagr | -0.1751 |
| net_avg_win | 77.6872 |
| net_avg_loss | -95.6280 |
| avg_hold_time_bars | 34.9938 |
| exposure | 0.5106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
