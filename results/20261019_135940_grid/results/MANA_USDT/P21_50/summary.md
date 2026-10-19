# EMA Hourly Continuation — MANA/USDT P21_50

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.5115 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.9294 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -8.3535 |
| sortino_ratio | -3.7159 |
| max_drawdown | 0.9907 |
| cagr | -0.8412 |
| net_avg_win | 24.1143 |
| net_avg_loss | -36.1979 |
| avg_hold_time_bars | 4.7232 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
