# EMA Hourly Continuation — ARPA/USDT P8_34

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1430 |
| net_profit_factor | 0.5270 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -9.8432 |
| sortino_ratio | -5.2322 |
| max_drawdown | 0.9985 |
| cagr | -0.9232 |
| net_avg_win | 18.3257 |
| net_avg_loss | -25.6480 |
| avg_hold_time_bars | 5.5196 |
| exposure | 0.3572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
