# EMA Hourly Continuation — BTC/USDT P26_144

**Symbol:** BTC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.4810 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 1.0462 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -4.9502 |
| sortino_ratio | -1.4571 |
| max_drawdown | 0.8809 |
| cagr | -0.5229 |
| net_avg_win | 34.5166 |
| net_avg_loss | -62.4949 |
| avg_hold_time_bars | 22.9566 |
| exposure | 0.4656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
