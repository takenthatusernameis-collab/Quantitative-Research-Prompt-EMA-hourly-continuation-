# EMA Hourly Continuation — PUFFER/USDT P12_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9887 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.4936 |
| sortino_ratio | -0.4179 |
| max_drawdown | 0.3689 |
| cagr | -0.1793 |
| net_avg_win | 74.6537 |
| net_avg_loss | -94.0375 |
| avg_hold_time_bars | 40.8914 |
| exposure | 0.7243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
