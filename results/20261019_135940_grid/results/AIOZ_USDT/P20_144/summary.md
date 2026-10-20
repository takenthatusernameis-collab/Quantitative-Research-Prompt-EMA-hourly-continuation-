# EMA Hourly Continuation — AIOZ/USDT P20_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.6836 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.8709 |
| sortino_ratio | -0.9595 |
| max_drawdown | 0.6995 |
| cagr | -0.3649 |
| net_avg_win | 53.6302 |
| net_avg_loss | -75.1642 |
| avg_hold_time_bars | 21.2732 |
| exposure | 0.5415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
