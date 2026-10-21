# EMA Hourly Continuation — RIO/USDT P26_144

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -1.4689 |
| sortino_ratio | -0.4094 |
| max_drawdown | 0.4047 |
| cagr | -0.1737 |
| net_avg_win | 78.6590 |
| net_avg_loss | -88.7934 |
| avg_hold_time_bars | 24.3141 |
| exposure | 0.4264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
