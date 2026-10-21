# EMA Hourly Continuation — BABYDOGE/USDT P89_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 20 |
| net_profit_factor | 1.3746 |
| net_win_rate | 0.6000 |
| gross_profit_factor | 1.4882 |
| gross_win_rate | 0.6000 |
| sharpe_ratio | 0.4531 |
| sortino_ratio | 0.0301 |
| max_drawdown | 0.0233 |
| cagr | 0.0124 |
| net_avg_win | 96.5574 |
| net_avg_loss | -105.3675 |
| avg_hold_time_bars | 20.7000 |
| exposure | 0.0187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
