# EMA Hourly Continuation — MOG/USDT P89_144

**Symbol:** MOG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.9258 |
| sortino_ratio | -1.2206 |
| max_drawdown | 0.7432 |
| cagr | -0.4389 |
| net_avg_win | 54.1526 |
| net_avg_loss | -74.8044 |
| avg_hold_time_bars | 5.0203 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
