# EMA Hourly Continuation — DGB/USDT P21_50

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1108 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.4206 |
| gross_profit_factor | 0.8095 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -9.5096 |
| sortino_ratio | -4.4550 |
| max_drawdown | 0.9966 |
| cagr | -0.8951 |
| net_avg_win | 15.3159 |
| net_avg_loss | -26.6394 |
| avg_hold_time_bars | 4.0054 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
