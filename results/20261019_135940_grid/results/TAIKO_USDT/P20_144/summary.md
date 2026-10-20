# EMA Hourly Continuation — TAIKO/USDT P20_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6223 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.1921 |
| sortino_ratio | -0.9359 |
| max_drawdown | 0.6779 |
| cagr | -0.3636 |
| net_avg_win | 55.9126 |
| net_avg_loss | -78.8694 |
| avg_hold_time_bars | 28.4892 |
| exposure | 0.5679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
