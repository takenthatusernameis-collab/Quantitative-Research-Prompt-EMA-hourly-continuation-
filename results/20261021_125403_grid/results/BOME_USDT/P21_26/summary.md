# EMA Hourly Continuation — BOME/USDT P21_26

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.8512 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1188 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -0.6351 |
| sortino_ratio | -0.1188 |
| max_drawdown | 0.2214 |
| cagr | -0.0541 |
| net_avg_win | 83.8350 |
| net_avg_loss | -110.9590 |
| avg_hold_time_bars | 4.5536 |
| exposure | 0.0348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
