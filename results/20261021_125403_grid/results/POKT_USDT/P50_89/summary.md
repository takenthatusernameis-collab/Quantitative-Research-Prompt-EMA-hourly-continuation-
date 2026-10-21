# EMA Hourly Continuation — POKT/USDT P50_89

**Symbol:** POKT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6026 |
| net_win_rate | 0.4255 |
| gross_profit_factor | 0.8107 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -3.5760 |
| sortino_ratio | -0.9797 |
| max_drawdown | 0.6976 |
| cagr | -0.3653 |
| net_avg_win | 64.6513 |
| net_avg_loss | -79.4770 |
| avg_hold_time_bars | 9.4335 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
