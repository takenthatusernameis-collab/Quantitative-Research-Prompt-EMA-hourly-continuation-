# EMA Hourly Continuation — IOST/USDT P12_26

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1323 |
| net_profit_factor | 0.3151 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.8346 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -11.4063 |
| sortino_ratio | -5.8885 |
| max_drawdown | 0.9995 |
| cagr | -0.9497 |
| net_avg_win | 8.2560 |
| net_avg_loss | -19.0511 |
| avg_hold_time_bars | 3.8307 |
| exposure | 0.2304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
