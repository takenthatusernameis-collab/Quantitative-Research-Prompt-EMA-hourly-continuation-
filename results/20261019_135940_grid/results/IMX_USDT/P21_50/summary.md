# EMA Hourly Continuation — IMX/USDT P21_50

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.5042 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8677 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -6.1570 |
| sortino_ratio | -2.6795 |
| max_drawdown | 0.9651 |
| cagr | -0.7312 |
| net_avg_win | 21.8294 |
| net_avg_loss | -37.4525 |
| avg_hold_time_bars | 4.6880 |
| exposure | 0.2053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
