# EMA Hourly Continuation — REQ/USDT P12_26

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1528 |
| net_profit_factor | 0.3589 |
| net_win_rate | 0.3685 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -15.5372 |
| sortino_ratio | -8.8037 |
| max_drawdown | 1.0000 |
| cagr | -0.9893 |
| net_avg_win | 9.9417 |
| net_avg_loss | -16.1628 |
| avg_hold_time_bars | 3.2094 |
| exposure | 0.2229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
