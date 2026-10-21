# EMA Hourly Continuation — MINA/USDT P8_89

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.8598 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0611 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -0.9733 |
| sortino_ratio | -0.3309 |
| max_drawdown | 0.4216 |
| cagr | -0.1450 |
| net_avg_win | 68.5454 |
| net_avg_loss | -86.5633 |
| avg_hold_time_bars | 24.9964 |
| exposure | 0.6351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
