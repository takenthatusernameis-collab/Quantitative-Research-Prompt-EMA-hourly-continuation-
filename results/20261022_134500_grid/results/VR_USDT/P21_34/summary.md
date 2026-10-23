# EMA Hourly Continuation — VR/USDT P21_34

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1217 |
| net_profit_factor | 0.2872 |
| net_win_rate | 0.2671 |
| gross_profit_factor | 0.5608 |
| gross_win_rate | 0.2917 |
| sharpe_ratio | -18.3563 |
| sortino_ratio | -9.5798 |
| max_drawdown | 1.0000 |
| cagr | -0.9966 |
| net_avg_win | 12.3957 |
| net_avg_loss | -15.7271 |
| avg_hold_time_bars | 2.8480 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
