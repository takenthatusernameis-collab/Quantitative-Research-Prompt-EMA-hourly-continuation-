# EMA Hourly Continuation — CFX/USDT P20_50

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6003 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.7962 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -3.4802 |
| sortino_ratio | -1.0934 |
| max_drawdown | 0.7322 |
| cagr | -0.3949 |
| net_avg_win | 49.3783 |
| net_avg_loss | -66.6648 |
| avg_hold_time_bars | 7.9569 |
| exposure | 0.1761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
