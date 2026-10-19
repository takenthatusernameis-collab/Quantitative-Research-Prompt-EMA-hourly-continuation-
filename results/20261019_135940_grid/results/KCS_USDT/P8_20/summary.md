# EMA Hourly Continuation — KCS/USDT P8_20

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1597 |
| net_profit_factor | 0.1415 |
| net_win_rate | 0.2905 |
| gross_profit_factor | 0.6733 |
| gross_win_rate | 0.3732 |
| sharpe_ratio | -21.2154 |
| sortino_ratio | -12.9512 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 3.5511 |
| net_avg_loss | -10.2804 |
| avg_hold_time_bars | 3.5529 |
| exposure | 0.2579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
