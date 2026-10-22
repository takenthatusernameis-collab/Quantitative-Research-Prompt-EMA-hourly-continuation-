# EMA Hourly Continuation — WIF/USDT P8_100

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6502 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.5521 |
| sortino_ratio | -1.2939 |
| max_drawdown | 0.7918 |
| cagr | -0.4593 |
| net_avg_win | 46.2722 |
| net_avg_loss | -63.7019 |
| avg_hold_time_bars | 21.6966 |
| exposure | 0.6598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
