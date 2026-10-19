# EMA Hourly Continuation — JST/USDT P12_20

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1204 |
| net_profit_factor | 0.0906 |
| net_win_rate | 0.3422 |
| gross_profit_factor | 0.6126 |
| gross_win_rate | 0.4493 |
| sharpe_ratio | -16.1548 |
| sortino_ratio | -8.4000 |
| max_drawdown | 1.0000 |
| cagr | -0.9900 |
| net_avg_win | 2.4170 |
| net_avg_loss | -13.8835 |
| avg_hold_time_bars | 2.8796 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
