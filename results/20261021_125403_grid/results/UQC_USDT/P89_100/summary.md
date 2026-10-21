# EMA Hourly Continuation — UQC/USDT P89_100

**Symbol:** UQC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.1618 |
| net_win_rate | 0.1675 |
| gross_profit_factor | 0.2998 |
| gross_win_rate | 0.2105 |
| sharpe_ratio | -8.1326 |
| sortino_ratio | -1.7662 |
| max_drawdown | 0.9155 |
| cagr | -0.6233 |
| net_avg_win | 50.4551 |
| net_avg_loss | -62.7232 |
| avg_hold_time_bars | 18.2201 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
