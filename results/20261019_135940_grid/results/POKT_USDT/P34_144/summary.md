# EMA Hourly Continuation — POKT/USDT P34_144

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4201 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -5.2252 |
| sortino_ratio | -1.8823 |
| max_drawdown | 0.8947 |
| cagr | -0.5890 |
| net_avg_win | 44.5457 |
| net_avg_loss | -55.7302 |
| avg_hold_time_bars | 13.4018 |
| exposure | 0.3985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
