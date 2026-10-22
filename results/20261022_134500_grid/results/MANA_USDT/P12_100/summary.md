# EMA Hourly Continuation — MANA/USDT P12_100

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.6033 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -5.1106 |
| sortino_ratio | -1.7219 |
| max_drawdown | 0.8935 |
| cagr | -0.5819 |
| net_avg_win | 51.1642 |
| net_avg_loss | -68.6761 |
| avg_hold_time_bars | 23.0153 |
| exposure | 0.6172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
