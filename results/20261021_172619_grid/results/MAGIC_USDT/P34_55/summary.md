# EMA Hourly Continuation — MAGIC/USDT P34_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6976 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 1.0069 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.7163 |
| sortino_ratio | -0.8323 |
| max_drawdown | 0.6267 |
| cagr | -0.3169 |
| net_avg_win | 63.1671 |
| net_avg_loss | -87.8155 |
| avg_hold_time_bars | 5.5164 |
| exposure | 0.1146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
