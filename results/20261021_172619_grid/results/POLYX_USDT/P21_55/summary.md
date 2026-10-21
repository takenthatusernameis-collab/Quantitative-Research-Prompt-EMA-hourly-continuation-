# EMA Hourly Continuation — POLYX/USDT P21_55

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.7237 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9974 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.7795 |
| sortino_ratio | -0.9660 |
| max_drawdown | 0.6979 |
| cagr | -0.3577 |
| net_avg_win | 60.3847 |
| net_avg_loss | -81.2091 |
| avg_hold_time_bars | 7.8254 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
