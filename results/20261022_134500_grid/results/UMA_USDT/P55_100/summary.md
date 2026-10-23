# EMA Hourly Continuation — UMA/USDT P55_100

**Symbol:** UMA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.5489 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -4.5203 |
| sortino_ratio | -1.6007 |
| max_drawdown | 0.8558 |
| cagr | -0.5305 |
| net_avg_win | 34.5993 |
| net_avg_loss | -59.0826 |
| avg_hold_time_bars | 6.1375 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
