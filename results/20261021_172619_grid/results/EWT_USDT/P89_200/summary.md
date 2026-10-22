# EMA Hourly Continuation — EWT/USDT P89_200

**Symbol:** EWT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.6736 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8257 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -1.8896 |
| sortino_ratio | -0.4242 |
| max_drawdown | 0.4217 |
| cagr | -0.1780 |
| net_avg_win | 70.3850 |
| net_avg_loss | -87.5891 |
| avg_hold_time_bars | 14.8080 |
| exposure | 0.1683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
