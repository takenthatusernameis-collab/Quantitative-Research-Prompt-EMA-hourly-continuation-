# EMA Hourly Continuation — DEXE/USDT P21_55

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7571 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0055 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.8535 |
| sortino_ratio | -0.5771 |
| max_drawdown | 0.5131 |
| cagr | -0.2330 |
| net_avg_win | 63.9605 |
| net_avg_loss | -85.2021 |
| avg_hold_time_bars | 13.8708 |
| exposure | 0.2976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
