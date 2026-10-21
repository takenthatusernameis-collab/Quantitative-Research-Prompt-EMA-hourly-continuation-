# EMA Hourly Continuation — ALT/USDT P50_89

**Symbol:** ALT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6835 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9170 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.2627 |
| sortino_ratio | -0.6380 |
| max_drawdown | 0.5327 |
| cagr | -0.2534 |
| net_avg_win | 59.7049 |
| net_avg_loss | -81.7076 |
| avg_hold_time_bars | 8.0720 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
