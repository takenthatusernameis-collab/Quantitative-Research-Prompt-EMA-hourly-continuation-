# EMA Hourly Continuation — MOG/USDT P8_21

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7823 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.9855 |
| sortino_ratio | -0.6589 |
| max_drawdown | 0.5169 |
| cagr | -0.2623 |
| net_avg_win | 74.6685 |
| net_avg_loss | -92.0199 |
| avg_hold_time_bars | 6.2312 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
