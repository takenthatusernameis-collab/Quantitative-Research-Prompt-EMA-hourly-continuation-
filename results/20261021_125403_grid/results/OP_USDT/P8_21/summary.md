# EMA Hourly Continuation — OP/USDT P8_21

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.8250 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1213 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -1.2874 |
| sortino_ratio | -0.4387 |
| max_drawdown | 0.4626 |
| cagr | -0.1836 |
| net_avg_win | 63.5690 |
| net_avg_loss | -88.0652 |
| avg_hold_time_bars | 5.5315 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
