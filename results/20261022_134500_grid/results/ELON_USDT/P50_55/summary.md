# EMA Hourly Continuation — ELON/USDT P50_55

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.1281 |
| net_win_rate | 0.3106 |
| gross_profit_factor | 0.4285 |
| gross_win_rate | 0.3307 |
| sharpe_ratio | -11.9486 |
| sortino_ratio | -4.5135 |
| max_drawdown | 0.9976 |
| cagr | -0.9088 |
| net_avg_win | 7.3259 |
| net_avg_loss | -25.7674 |
| avg_hold_time_bars | 2.1227 |
| exposure | 0.0621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
