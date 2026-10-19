# EMA Hourly Continuation — CRV/USDT P50_144

**Symbol:** CRV/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.6085 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.8206 |
| sortino_ratio | -1.2776 |
| max_drawdown | 0.7902 |
| cagr | -0.4563 |
| net_avg_win | 45.9479 |
| net_avg_loss | -67.1536 |
| avg_hold_time_bars | 9.6732 |
| exposure | 0.2475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
