# EMA Hourly Continuation — BSV/USDT P20_100

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5250 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -6.1685 |
| sortino_ratio | -2.3090 |
| max_drawdown | 0.9435 |
| cagr | -0.6770 |
| net_avg_win | 33.8891 |
| net_avg_loss | -48.2201 |
| avg_hold_time_bars | 14.0543 |
| exposure | 0.4587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
