# EMA Hourly Continuation — EGLD/USDT P12_200

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8828 |
| net_win_rate | 0.5181 |
| gross_profit_factor | 1.0637 |
| gross_win_rate | 0.5181 |
| sharpe_ratio | -0.6419 |
| sortino_ratio | -0.1681 |
| max_drawdown | 0.3236 |
| cagr | -0.0776 |
| net_avg_win | 80.3981 |
| net_avg_loss | -97.8970 |
| avg_hold_time_bars | 47.5843 |
| exposure | 0.7181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
