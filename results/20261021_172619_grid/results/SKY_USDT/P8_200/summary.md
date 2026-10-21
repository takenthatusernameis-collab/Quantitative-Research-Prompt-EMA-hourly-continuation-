# EMA Hourly Continuation — SKY/USDT P8_200

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.9284 |
| net_win_rate | 0.5276 |
| gross_profit_factor | 1.1030 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -0.4028 |
| sortino_ratio | -0.1093 |
| max_drawdown | 0.3303 |
| cagr | -0.0535 |
| net_avg_win | 90.2792 |
| net_avg_loss | -108.5959 |
| avg_hold_time_bars | 46.0690 |
| exposure | 0.7450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
