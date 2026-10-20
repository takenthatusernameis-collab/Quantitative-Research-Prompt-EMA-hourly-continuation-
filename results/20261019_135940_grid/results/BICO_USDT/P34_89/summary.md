# EMA Hourly Continuation — BICO/USDT P34_89

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.7905 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -4.5501 |
| sortino_ratio | -1.6537 |
| max_drawdown | 0.8606 |
| cagr | -0.5397 |
| net_avg_win | 32.2769 |
| net_avg_loss | -49.9817 |
| avg_hold_time_bars | 8.9713 |
| exposure | 0.2700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
