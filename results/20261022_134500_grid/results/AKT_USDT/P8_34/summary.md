# EMA Hourly Continuation — AKT/USDT P8_34

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1349 |
| net_profit_factor | 0.5290 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -8.4259 |
| sortino_ratio | -4.3386 |
| max_drawdown | 0.9956 |
| cagr | -0.8804 |
| net_avg_win | 18.9475 |
| net_avg_loss | -27.8402 |
| avg_hold_time_bars | 5.1801 |
| exposure | 0.3176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
