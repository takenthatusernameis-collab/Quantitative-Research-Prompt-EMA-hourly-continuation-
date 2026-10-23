# EMA Hourly Continuation — WOO/USDT P20_50

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -6.2625 |
| sortino_ratio | -2.6984 |
| max_drawdown | 0.9647 |
| cagr | -0.7296 |
| net_avg_win | 31.9688 |
| net_avg_loss | -46.1618 |
| avg_hold_time_bars | 5.4041 |
| exposure | 0.2304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
