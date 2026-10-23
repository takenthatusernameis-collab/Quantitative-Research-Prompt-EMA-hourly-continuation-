# EMA Hourly Continuation — ELON/USDT P144_200

**Symbol:** ELON/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.3300 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.5931 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -5.5646 |
| sortino_ratio | -1.6309 |
| max_drawdown | 0.8652 |
| cagr | -0.5469 |
| net_avg_win | 23.6138 |
| net_avg_loss | -53.0076 |
| avg_hold_time_bars | 4.4090 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
