# EMA Hourly Continuation — ONT/USDT P8_21

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1578 |
| net_profit_factor | 0.4293 |
| net_win_rate | 0.4176 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -12.3978 |
| sortino_ratio | -6.9404 |
| max_drawdown | 0.9999 |
| cagr | -0.9711 |
| net_avg_win | 11.4130 |
| net_avg_loss | -19.0640 |
| avg_hold_time_bars | 3.3302 |
| exposure | 0.2378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
