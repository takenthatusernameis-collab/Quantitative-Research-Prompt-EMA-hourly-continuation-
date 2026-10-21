# EMA Hourly Continuation — JTO/USDT P12_34

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.8293 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0628 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.6810 |
| sortino_ratio | -0.6137 |
| max_drawdown | 0.5893 |
| cagr | -0.2469 |
| net_avg_win | 75.2055 |
| net_avg_loss | -94.1207 |
| avg_hold_time_bars | 7.2879 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
