# EMA Hourly Continuation — ZETA/USDT P20_55

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 939 |
| net_profit_factor | 0.5645 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -6.5666 |
| sortino_ratio | -2.8286 |
| max_drawdown | 0.9685 |
| cagr | -0.7454 |
| net_avg_win | 29.6709 |
| net_avg_loss | -43.0883 |
| avg_hold_time_bars | 6.3174 |
| exposure | 0.2684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
