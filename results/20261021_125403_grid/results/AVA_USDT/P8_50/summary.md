# EMA Hourly Continuation — AVA/USDT P8_50

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.7925 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.8442 |
| sortino_ratio | -0.7012 |
| max_drawdown | 0.6153 |
| cagr | -0.2766 |
| net_avg_win | 59.7014 |
| net_avg_loss | -77.5106 |
| avg_hold_time_bars | 12.1182 |
| exposure | 0.3867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
