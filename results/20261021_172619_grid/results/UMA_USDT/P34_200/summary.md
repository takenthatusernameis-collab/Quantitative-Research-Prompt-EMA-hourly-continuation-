# EMA Hourly Continuation — UMA/USDT P34_200

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7848 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.3818 |
| sortino_ratio | -0.3693 |
| max_drawdown | 0.3684 |
| cagr | -0.1569 |
| net_avg_win | 73.0582 |
| net_avg_loss | -92.0359 |
| avg_hold_time_bars | 29.9457 |
| exposure | 0.4764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
