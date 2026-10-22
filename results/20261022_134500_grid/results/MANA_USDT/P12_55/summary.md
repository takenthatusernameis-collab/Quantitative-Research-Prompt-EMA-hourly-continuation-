# EMA Hourly Continuation — MANA/USDT P12_55

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5691 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.9685 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -7.2190 |
| sortino_ratio | -3.2315 |
| max_drawdown | 0.9825 |
| cagr | -0.7957 |
| net_avg_win | 28.5522 |
| net_avg_loss | -40.8198 |
| avg_hold_time_bars | 8.3636 |
| exposure | 0.3847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
