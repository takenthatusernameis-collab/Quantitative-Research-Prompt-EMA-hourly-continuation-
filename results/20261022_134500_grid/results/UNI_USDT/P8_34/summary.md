# EMA Hourly Continuation — UNI/USDT P8_34

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.5189 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -9.1721 |
| sortino_ratio | -4.8119 |
| max_drawdown | 0.9976 |
| cagr | -0.9092 |
| net_avg_win | 17.3229 |
| net_avg_loss | -26.5472 |
| avg_hold_time_bars | 5.1091 |
| exposure | 0.3256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
