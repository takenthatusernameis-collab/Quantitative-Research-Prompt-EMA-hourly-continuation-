# EMA Hourly Continuation — BICO/USDT P20_50

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -3.4877 |
| sortino_ratio | -1.2261 |
| max_drawdown | 0.7666 |
| cagr | -0.4297 |
| net_avg_win | 44.3402 |
| net_avg_loss | -60.7143 |
| avg_hold_time_bars | 7.6765 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
