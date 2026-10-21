# EMA Hourly Continuation — ORDI/USDT P20_26

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.7075 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9563 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.4614 |
| sortino_ratio | -0.2825 |
| max_drawdown | 0.2849 |
| cagr | -0.1218 |
| net_avg_win | 75.6431 |
| net_avg_loss | -102.3177 |
| avg_hold_time_bars | 5.0934 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
