# EMA Hourly Continuation — BSV/USDT P8_26

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.6488 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -4.1428 |
| sortino_ratio | -1.5715 |
| max_drawdown | 0.8411 |
| cagr | -0.5129 |
| net_avg_win | 46.6492 |
| net_avg_loss | -64.1461 |
| avg_hold_time_bars | 6.4003 |
| exposure | 0.2042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
