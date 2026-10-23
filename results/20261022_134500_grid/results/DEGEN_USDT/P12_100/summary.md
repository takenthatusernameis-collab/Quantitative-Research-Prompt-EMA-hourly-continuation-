# EMA Hourly Continuation — DEGEN/USDT P12_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.7271 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9637 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.1538 |
| sortino_ratio | -1.1216 |
| max_drawdown | 0.7727 |
| cagr | -0.4136 |
| net_avg_win | 64.8499 |
| net_avg_loss | -80.9162 |
| avg_hold_time_bars | 19.7991 |
| exposure | 0.5742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
