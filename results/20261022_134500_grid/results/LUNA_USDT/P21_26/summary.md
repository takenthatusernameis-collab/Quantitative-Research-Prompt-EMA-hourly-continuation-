# EMA Hourly Continuation — LUNA/USDT P21_26

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1295 |
| net_profit_factor | 0.2207 |
| net_win_rate | 0.3259 |
| gross_profit_factor | 0.7657 |
| gross_win_rate | 0.3892 |
| sharpe_ratio | -16.9114 |
| sortino_ratio | -8.9975 |
| max_drawdown | 1.0000 |
| cagr | -0.9932 |
| net_avg_win | 6.7108 |
| net_avg_loss | -14.6987 |
| avg_hold_time_bars | 1.7931 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
