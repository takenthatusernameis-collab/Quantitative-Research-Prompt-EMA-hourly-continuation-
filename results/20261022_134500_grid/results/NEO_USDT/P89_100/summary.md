# EMA Hourly Continuation — NEO/USDT P89_100

**Symbol:** NEO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.1970 |
| net_win_rate | 0.3469 |
| gross_profit_factor | 0.6935 |
| gross_win_rate | 0.4129 |
| sharpe_ratio | -11.1416 |
| sortino_ratio | -4.1697 |
| max_drawdown | 0.9965 |
| cagr | -0.8941 |
| net_avg_win | 11.0584 |
| net_avg_loss | -29.8278 |
| avg_hold_time_bars | 2.1397 |
| exposure | 0.0620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
