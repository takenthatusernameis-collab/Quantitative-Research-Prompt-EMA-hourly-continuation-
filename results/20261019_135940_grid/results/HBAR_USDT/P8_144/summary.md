# EMA Hourly Continuation — HBAR/USDT P8_144

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6780 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 1.0260 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9336 |
| sortino_ratio | -0.8862 |
| max_drawdown | 0.7004 |
| cagr | -0.3495 |
| net_avg_win | 61.2484 |
| net_avg_loss | -86.5274 |
| avg_hold_time_bars | 36.4009 |
| exposure | 0.7677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
