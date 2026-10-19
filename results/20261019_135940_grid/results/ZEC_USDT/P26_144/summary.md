# EMA Hourly Continuation — ZEC/USDT P26_144

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8044 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.1286 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -1.4901 |
| sortino_ratio | -0.4608 |
| max_drawdown | 0.4487 |
| cagr | -0.1976 |
| net_avg_win | 69.8818 |
| net_avg_loss | -96.0986 |
| avg_hold_time_bars | 20.6197 |
| exposure | 0.4461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
