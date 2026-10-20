# EMA Hourly Continuation — AXL/USDT P34_55

**Symbol:** AXL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.4745 |
| net_win_rate | 0.4198 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -8.1866 |
| sortino_ratio | -3.5497 |
| max_drawdown | 0.9879 |
| cagr | -0.8222 |
| net_avg_win | 22.5650 |
| net_avg_loss | -34.4046 |
| avg_hold_time_bars | 3.5356 |
| exposure | 0.1505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
