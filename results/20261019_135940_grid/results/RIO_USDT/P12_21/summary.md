# EMA Hourly Continuation — RIO/USDT P12_21

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1553 |
| net_profit_factor | 0.4095 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.7301 |
| gross_win_rate | 0.3883 |
| sharpe_ratio | -12.7255 |
| sortino_ratio | -7.0676 |
| max_drawdown | 0.9999 |
| cagr | -0.9728 |
| net_avg_win | 11.8117 |
| net_avg_loss | -17.5282 |
| avg_hold_time_bars | 2.3793 |
| exposure | 0.1696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
