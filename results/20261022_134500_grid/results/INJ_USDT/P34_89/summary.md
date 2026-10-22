# EMA Hourly Continuation — INJ/USDT P34_89

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.5617 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -5.1093 |
| sortino_ratio | -1.9012 |
| max_drawdown | 0.9026 |
| cagr | -0.6029 |
| net_avg_win | 36.3396 |
| net_avg_loss | -53.4354 |
| avg_hold_time_bars | 7.0825 |
| exposure | 0.2263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
