# EMA Hourly Continuation — POPCAT/USDT P21_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8064 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -1.9797 |
| sortino_ratio | -0.5376 |
| max_drawdown | 0.4437 |
| cagr | -0.2201 |
| net_avg_win | 70.4941 |
| net_avg_loss | -81.8206 |
| avg_hold_time_bars | 32.5426 |
| exposure | 0.5450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
