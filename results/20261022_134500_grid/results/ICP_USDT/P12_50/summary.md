# EMA Hourly Continuation — ICP/USDT P12_50

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1095 |
| net_profit_factor | 0.5005 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8520 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -7.1206 |
| sortino_ratio | -3.2847 |
| max_drawdown | 0.9841 |
| cagr | -0.8050 |
| net_avg_win | 19.6704 |
| net_avg_loss | -33.1480 |
| avg_hold_time_bars | 6.5982 |
| exposure | 0.3284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
