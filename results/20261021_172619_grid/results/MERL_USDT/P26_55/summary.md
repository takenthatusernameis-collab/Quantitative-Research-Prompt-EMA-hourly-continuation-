# EMA Hourly Continuation — MERL/USDT P26_55

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7289 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.0308 |
| sortino_ratio | -0.6017 |
| max_drawdown | 0.5174 |
| cagr | -0.2420 |
| net_avg_win | 65.3018 |
| net_avg_loss | -82.0278 |
| avg_hold_time_bars | 8.1137 |
| exposure | 0.1594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
