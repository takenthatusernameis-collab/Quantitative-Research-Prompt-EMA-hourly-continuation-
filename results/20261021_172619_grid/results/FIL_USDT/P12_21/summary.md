# EMA Hourly Continuation — FIL/USDT P12_21

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6188 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.3602 |
| sortino_ratio | -0.5556 |
| max_drawdown | 0.4970 |
| cagr | -0.2242 |
| net_avg_win | 59.7641 |
| net_avg_loss | -87.0652 |
| avg_hold_time_bars | 4.9074 |
| exposure | 0.0602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
