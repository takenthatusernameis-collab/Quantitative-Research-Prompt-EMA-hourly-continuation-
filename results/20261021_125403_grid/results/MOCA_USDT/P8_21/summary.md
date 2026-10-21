# EMA Hourly Continuation — MOCA/USDT P8_21

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6003 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8336 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -3.5058 |
| sortino_ratio | -1.2412 |
| max_drawdown | 0.7393 |
| cagr | -0.4337 |
| net_avg_win | 41.3020 |
| net_avg_loss | -62.2052 |
| avg_hold_time_bars | 5.6241 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
