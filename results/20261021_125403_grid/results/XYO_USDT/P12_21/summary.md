# EMA Hourly Continuation — XYO/USDT P12_21

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4617 |
| net_win_rate | 0.4053 |
| gross_profit_factor | 0.7136 |
| gross_win_rate | 0.4053 |
| sharpe_ratio | -5.2214 |
| sortino_ratio | -1.5240 |
| max_drawdown | 0.8337 |
| cagr | -0.5075 |
| net_avg_win | 42.2401 |
| net_avg_loss | -62.3510 |
| avg_hold_time_bars | 5.4652 |
| exposure | 0.1031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
