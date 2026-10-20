# EMA Hourly Continuation — AVA/USDT P26_144

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.6302 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -2.7953 |
| sortino_ratio | -0.9087 |
| max_drawdown | 0.6872 |
| cagr | -0.3538 |
| net_avg_win | 42.6630 |
| net_avg_loss | -67.4484 |
| avg_hold_time_bars | 18.1107 |
| exposure | 0.4388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
