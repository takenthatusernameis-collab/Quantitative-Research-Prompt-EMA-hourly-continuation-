# EMA Hourly Continuation — DCR/USDT P89_200

**Symbol:** DCR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5012 |
| net_win_rate | 0.4329 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -4.3880 |
| sortino_ratio | -1.2837 |
| max_drawdown | 0.7862 |
| cagr | -0.4565 |
| net_avg_win | 42.1907 |
| net_avg_loss | -64.2513 |
| avg_hold_time_bars | 10.3333 |
| exposure | 0.2020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
