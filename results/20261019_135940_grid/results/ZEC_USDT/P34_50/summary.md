# EMA Hourly Continuation — ZEC/USDT P34_50

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.3611 |
| net_win_rate | 0.4122 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4335 |
| sharpe_ratio | -8.9975 |
| sortino_ratio | -3.6884 |
| max_drawdown | 0.9918 |
| cagr | -0.8515 |
| net_avg_win | 16.0147 |
| net_avg_loss | -31.1061 |
| avg_hold_time_bars | 2.2827 |
| exposure | 0.0881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
