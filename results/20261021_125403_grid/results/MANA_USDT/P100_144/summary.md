# EMA Hourly Continuation — MANA/USDT P100_144

**Symbol:** MANA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.6426 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9144 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.2096 |
| sortino_ratio | -0.5100 |
| max_drawdown | 0.4656 |
| cagr | -0.2080 |
| net_avg_win | 64.2592 |
| net_avg_loss | -91.8553 |
| avg_hold_time_bars | 5.3050 |
| exposure | 0.0625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
