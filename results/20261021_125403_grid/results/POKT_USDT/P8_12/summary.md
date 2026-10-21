# EMA Hourly Continuation — POKT/USDT P8_12

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5163 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.7475 |
| gross_win_rate | 0.3869 |
| sharpe_ratio | -5.3473 |
| sortino_ratio | -1.5941 |
| max_drawdown | 0.8498 |
| cagr | -0.5233 |
| net_avg_win | 52.7935 |
| net_avg_loss | -64.5188 |
| avg_hold_time_bars | 4.5362 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
