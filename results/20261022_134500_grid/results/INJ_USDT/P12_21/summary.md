# EMA Hourly Continuation — INJ/USDT P12_21

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1531 |
| net_profit_factor | 0.3850 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8127 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -11.8741 |
| sortino_ratio | -6.5542 |
| max_drawdown | 0.9998 |
| cagr | -0.9657 |
| net_avg_win | 9.5558 |
| net_avg_loss | -18.5581 |
| avg_hold_time_bars | 2.3801 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
