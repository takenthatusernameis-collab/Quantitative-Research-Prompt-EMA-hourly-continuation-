# EMA Hourly Continuation — MANA/USDT P34_100

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6084 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 1.0168 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -5.3881 |
| sortino_ratio | -1.9399 |
| max_drawdown | 0.9147 |
| cagr | -0.6170 |
| net_avg_win | 46.9786 |
| net_avg_loss | -64.3845 |
| avg_hold_time_bars | 9.9698 |
| exposure | 0.3000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
