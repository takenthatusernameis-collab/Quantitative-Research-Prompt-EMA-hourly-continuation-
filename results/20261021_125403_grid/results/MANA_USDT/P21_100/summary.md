# EMA Hourly Continuation — MANA/USDT P21_100

**Symbol:** MANA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8393 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0659 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.2620 |
| sortino_ratio | -0.3817 |
| max_drawdown | 0.4342 |
| cagr | -0.1624 |
| net_avg_win | 82.3031 |
| net_avg_loss | -103.5087 |
| avg_hold_time_bars | 20.8829 |
| exposure | 0.4215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
