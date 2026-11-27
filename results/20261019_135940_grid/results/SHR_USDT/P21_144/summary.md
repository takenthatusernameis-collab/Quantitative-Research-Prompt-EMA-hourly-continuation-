# EMA Hourly Continuation — SHR/USDT P21_144

**Symbol:** SHR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 821 |
| net_profit_factor | 0.4288 |
| net_win_rate | 0.3362 |
| gross_profit_factor | 0.5601 |
| gross_win_rate | 0.3362 |
| sharpe_ratio | -8.0816 |
| sortino_ratio | -3.2239 |
| max_drawdown | 0.9795 |
| cagr | -0.7847 |
| net_avg_win | 26.6327 |
| net_avg_loss | -31.4549 |
| avg_hold_time_bars | 11.6541 |
| exposure | 0.4330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
