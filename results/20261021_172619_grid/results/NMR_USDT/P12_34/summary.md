# EMA Hourly Continuation — NMR/USDT P12_34

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -3.1681 |
| sortino_ratio | -1.1848 |
| max_drawdown | 0.7538 |
| cagr | -0.4187 |
| net_avg_win | 52.5476 |
| net_avg_loss | -71.8106 |
| avg_hold_time_bars | 6.4062 |
| exposure | 0.1986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
