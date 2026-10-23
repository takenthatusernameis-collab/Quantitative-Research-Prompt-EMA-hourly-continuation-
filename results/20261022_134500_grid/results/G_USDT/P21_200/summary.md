# EMA Hourly Continuation — G/USDT P21_200

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.5535 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 0.7623 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -3.4493 |
| sortino_ratio | -0.9242 |
| max_drawdown | 0.6502 |
| cagr | -0.3510 |
| net_avg_win | 55.4884 |
| net_avg_loss | -77.4684 |
| avg_hold_time_bars | 40.6603 |
| exposure | 0.6671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
