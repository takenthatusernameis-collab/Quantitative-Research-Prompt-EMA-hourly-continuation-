# EMA Hourly Continuation — DIA/USDT P8_21

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9410 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.3053 |
| sortino_ratio | -1.2566 |
| max_drawdown | 0.7665 |
| cagr | -0.4372 |
| net_avg_win | 43.0221 |
| net_avg_loss | -63.0802 |
| avg_hold_time_bars | 5.6071 |
| exposure | 0.1789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
