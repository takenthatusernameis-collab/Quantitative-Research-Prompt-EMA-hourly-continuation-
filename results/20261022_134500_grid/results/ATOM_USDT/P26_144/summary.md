# EMA Hourly Continuation — ATOM/USDT P26_144

**Symbol:** ATOM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6433 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9970 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.7785 |
| sortino_ratio | -0.8575 |
| max_drawdown | 0.6718 |
| cagr | -0.3409 |
| net_avg_win | 48.5697 |
| net_avg_loss | -74.2641 |
| avg_hold_time_bars | 21.7140 |
| exposure | 0.4797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
