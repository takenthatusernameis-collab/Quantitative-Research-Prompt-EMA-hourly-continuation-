# EMA Hourly Continuation — GMT/USDT P21_26

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.5841 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.1505 |
| sortino_ratio | -0.4191 |
| max_drawdown | 0.3865 |
| cagr | -0.1749 |
| net_avg_win | 62.5257 |
| net_avg_loss | -92.9932 |
| avg_hold_time_bars | 4.1189 |
| exposure | 0.0346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
