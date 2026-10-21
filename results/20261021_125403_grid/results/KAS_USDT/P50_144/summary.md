# EMA Hourly Continuation — KAS/USDT P50_144

**Symbol:** KAS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6660 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8473 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -2.1422 |
| sortino_ratio | -0.5626 |
| max_drawdown | 0.4885 |
| cagr | -0.2271 |
| net_avg_win | 59.3648 |
| net_avg_loss | -78.7934 |
| avg_hold_time_bars | 15.0059 |
| exposure | 0.2326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
