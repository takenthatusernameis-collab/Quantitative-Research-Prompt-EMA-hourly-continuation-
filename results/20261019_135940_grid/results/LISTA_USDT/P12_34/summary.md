# EMA Hourly Continuation — LISTA/USDT P12_34

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.5764 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -7.0306 |
| sortino_ratio | -3.3791 |
| max_drawdown | 0.9779 |
| cagr | -0.7999 |
| net_avg_win | 27.6314 |
| net_avg_loss | -38.7510 |
| avg_hold_time_bars | 5.0139 |
| exposure | 0.2638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
