# EMA Hourly Continuation — BICO/USDT P26_50

**Symbol:** BICO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.4227 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.7644 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -6.5696 |
| sortino_ratio | -2.7845 |
| max_drawdown | 0.9641 |
| cagr | -0.7337 |
| net_avg_win | 17.7754 |
| net_avg_loss | -33.4595 |
| avg_hold_time_bars | 4.5971 |
| exposure | 0.1872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
