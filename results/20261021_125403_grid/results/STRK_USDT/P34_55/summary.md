# EMA Hourly Continuation — STRK/USDT P34_55

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.7414 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.4437 |
| sortino_ratio | -0.3334 |
| max_drawdown | 0.3300 |
| cagr | -0.1414 |
| net_avg_win | 70.7035 |
| net_avg_loss | -94.6343 |
| avg_hold_time_bars | 5.5444 |
| exposure | 0.0653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
