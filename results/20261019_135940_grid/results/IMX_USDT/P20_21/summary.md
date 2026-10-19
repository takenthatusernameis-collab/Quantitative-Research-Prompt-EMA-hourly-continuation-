# EMA Hourly Continuation — IMX/USDT P20_21

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.1556 |
| net_win_rate | 0.3158 |
| gross_profit_factor | 0.5816 |
| gross_win_rate | 0.3865 |
| sharpe_ratio | -16.8969 |
| sortino_ratio | -8.7905 |
| max_drawdown | 1.0000 |
| cagr | -0.9931 |
| net_avg_win | 4.7997 |
| net_avg_loss | -14.2344 |
| avg_hold_time_bars | 1.6974 |
| exposure | 0.0934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
