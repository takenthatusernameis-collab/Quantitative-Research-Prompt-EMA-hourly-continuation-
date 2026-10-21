# EMA Hourly Continuation — BCH/USDT P20_26

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 150 |
| net_profit_factor | 0.7317 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1025 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -1.1597 |
| sortino_ratio | -0.2053 |
| max_drawdown | 0.2544 |
| cagr | -0.0889 |
| net_avg_win | 71.9843 |
| net_avg_loss | -109.4635 |
| avg_hold_time_bars | 6.0067 |
| exposure | 0.0410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
