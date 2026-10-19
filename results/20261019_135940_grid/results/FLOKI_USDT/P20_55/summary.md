# EMA Hourly Continuation — FLOKI/USDT P20_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.5430 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8872 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -7.3487 |
| sortino_ratio | -3.2825 |
| max_drawdown | 0.9852 |
| cagr | -0.8089 |
| net_avg_win | 25.3151 |
| net_avg_loss | -37.9874 |
| avg_hold_time_bars | 5.2566 |
| exposure | 0.2459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
