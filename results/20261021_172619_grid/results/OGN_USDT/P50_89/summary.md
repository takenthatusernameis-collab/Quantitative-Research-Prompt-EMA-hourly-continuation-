# EMA Hourly Continuation — OGN/USDT P50_89

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.2388 |
| sortino_ratio | -0.9698 |
| max_drawdown | 0.6780 |
| cagr | -0.3598 |
| net_avg_win | 55.8520 |
| net_avg_loss | -79.4262 |
| avg_hold_time_bars | 7.4943 |
| exposure | 0.1496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
