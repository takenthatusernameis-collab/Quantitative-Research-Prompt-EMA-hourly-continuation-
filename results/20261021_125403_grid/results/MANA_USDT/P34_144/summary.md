# EMA Hourly Continuation — MANA/USDT P34_144

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8654 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0824 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.8705 |
| sortino_ratio | -0.2405 |
| max_drawdown | 0.2753 |
| cagr | -0.1070 |
| net_avg_win | 82.8454 |
| net_avg_loss | -103.8416 |
| avg_hold_time_bars | 23.3794 |
| exposure | 0.3921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
