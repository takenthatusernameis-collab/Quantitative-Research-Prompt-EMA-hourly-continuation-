# EMA Hourly Continuation — KMNO/USDT P26_144

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6584 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9020 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.9103 |
| sortino_ratio | -0.8681 |
| max_drawdown | 0.6698 |
| cagr | -0.3414 |
| net_avg_win | 58.8290 |
| net_avg_loss | -80.2221 |
| avg_hold_time_bars | 21.3969 |
| exposure | 0.4406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
