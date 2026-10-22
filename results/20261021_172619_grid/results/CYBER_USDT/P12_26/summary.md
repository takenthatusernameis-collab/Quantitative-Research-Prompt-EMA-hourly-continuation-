# EMA Hourly Continuation — CYBER/USDT P12_26

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.7722 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1201 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -2.1148 |
| sortino_ratio | -0.7434 |
| max_drawdown | 0.5853 |
| cagr | -0.2895 |
| net_avg_win | 62.2009 |
| net_avg_loss | -89.6872 |
| avg_hold_time_bars | 5.9832 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
