# EMA Hourly Continuation — CAKE/USDT P8_26

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1511 |
| net_profit_factor | 0.3954 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 1.0067 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -11.5106 |
| sortino_ratio | -6.3284 |
| max_drawdown | 0.9997 |
| cagr | -0.9601 |
| net_avg_win | 10.0284 |
| net_avg_loss | -19.2496 |
| avg_hold_time_bars | 4.1284 |
| exposure | 0.2835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
