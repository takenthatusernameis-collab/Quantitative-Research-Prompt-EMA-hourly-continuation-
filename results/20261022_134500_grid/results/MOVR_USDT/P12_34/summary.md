# EMA Hourly Continuation — MOVR/USDT P12_34

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.4471 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.9211 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -8.5228 |
| sortino_ratio | -4.3718 |
| max_drawdown | 0.9958 |
| cagr | -0.8831 |
| net_avg_win | 13.5962 |
| net_avg_loss | -24.2959 |
| avg_hold_time_bars | 4.2686 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
