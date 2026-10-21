# EMA Hourly Continuation — ACE/USDT P89_144

**Symbol:** ACE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.7577 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0131 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.3613 |
| sortino_ratio | -0.3197 |
| max_drawdown | 0.3185 |
| cagr | -0.1366 |
| net_avg_win | 71.2061 |
| net_avg_loss | -96.0973 |
| avg_hold_time_bars | 8.8959 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
