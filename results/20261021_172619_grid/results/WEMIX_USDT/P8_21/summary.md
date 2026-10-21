# EMA Hourly Continuation — WEMIX/USDT P8_21

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.4733 |
| net_win_rate | 0.3704 |
| gross_profit_factor | 0.6407 |
| gross_win_rate | 0.3704 |
| sharpe_ratio | -4.9019 |
| sortino_ratio | -1.2999 |
| max_drawdown | 0.7850 |
| cagr | -0.4559 |
| net_avg_win | 54.1388 |
| net_avg_loss | -67.2830 |
| avg_hold_time_bars | 8.5499 |
| exposure | 0.1364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
