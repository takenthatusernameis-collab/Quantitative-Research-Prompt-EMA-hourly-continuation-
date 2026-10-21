# EMA Hourly Continuation — AXS/USDT P8_55

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.8407 |
| net_win_rate | 0.5195 |
| gross_profit_factor | 1.0747 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -1.3591 |
| sortino_ratio | -0.4838 |
| max_drawdown | 0.4587 |
| cagr | -0.2015 |
| net_avg_win | 71.4558 |
| net_avg_loss | -91.8841 |
| avg_hold_time_bars | 17.5731 |
| exposure | 0.4898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
