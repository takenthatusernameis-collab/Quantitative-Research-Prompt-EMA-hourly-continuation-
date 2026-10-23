# EMA Hourly Continuation — CARV/USDT P8_50

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.1051 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -4.2265 |
| sortino_ratio | -1.8260 |
| max_drawdown | 0.8407 |
| cagr | -0.5882 |
| net_avg_win | 41.3979 |
| net_avg_loss | -63.6728 |
| avg_hold_time_bars | 11.1850 |
| exposure | 0.4866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
