# EMA Hourly Continuation — SQD/USDT P89_200

**Symbol:** SQD/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8793 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0498 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.6593 |
| sortino_ratio | -0.1581 |
| max_drawdown | 0.2177 |
| cagr | -0.0724 |
| net_avg_win | 88.0854 |
| net_avg_loss | -104.7278 |
| avg_hold_time_bars | 14.0630 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
