# EMA Hourly Continuation — MANA/USDT P20_21

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.6067 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -1.5935 |
| sortino_ratio | -0.2538 |
| max_drawdown | 0.2657 |
| cagr | -0.1088 |
| net_avg_win | 65.6565 |
| net_avg_loss | -99.7666 |
| avg_hold_time_bars | 3.5122 |
| exposure | 0.0196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
