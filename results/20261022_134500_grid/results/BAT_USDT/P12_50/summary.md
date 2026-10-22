# EMA Hourly Continuation — BAT/USDT P12_50

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.5096 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.9436 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -6.7888 |
| sortino_ratio | -3.0806 |
| max_drawdown | 0.9762 |
| cagr | -0.7717 |
| net_avg_win | 21.8505 |
| net_avg_loss | -35.0243 |
| avg_hold_time_bars | 7.7500 |
| exposure | 0.3635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
