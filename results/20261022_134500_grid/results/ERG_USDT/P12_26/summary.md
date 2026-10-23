# EMA Hourly Continuation — ERG/USDT P12_26

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1431 |
| net_profit_factor | 0.2254 |
| net_win_rate | 0.3054 |
| gross_profit_factor | 0.5033 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -16.5369 |
| sortino_ratio | -9.0780 |
| max_drawdown | 1.0000 |
| cagr | -0.9904 |
| net_avg_win | 6.6570 |
| net_avg_loss | -12.9869 |
| avg_hold_time_bars | 2.9546 |
| exposure | 0.1922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
