# EMA Hourly Continuation — TNSR/USDT P8_200

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7194 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9703 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.4434 |
| sortino_ratio | -0.6918 |
| max_drawdown | 0.5845 |
| cagr | -0.2809 |
| net_avg_win | 74.2539 |
| net_avg_loss | -93.6105 |
| avg_hold_time_bars | 41.8610 |
| exposure | 0.7767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
