# EMA Hourly Continuation — STRAX/USDT P50_144

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6517 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -3.0808 |
| sortino_ratio | -0.8814 |
| max_drawdown | 0.6399 |
| cagr | -0.3339 |
| net_avg_win | 64.4663 |
| net_avg_loss | -83.9487 |
| avg_hold_time_bars | 14.1464 |
| exposure | 0.2607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
