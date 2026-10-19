# EMA Hourly Continuation — QNT/USDT P8_26

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1667 |
| net_profit_factor | 0.2973 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7287 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -12.4117 |
| sortino_ratio | -7.1921 |
| max_drawdown | 0.9999 |
| cagr | -0.9727 |
| net_avg_win | 6.0786 |
| net_avg_loss | -14.6545 |
| avg_hold_time_bars | 3.5033 |
| exposure | 0.2655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
