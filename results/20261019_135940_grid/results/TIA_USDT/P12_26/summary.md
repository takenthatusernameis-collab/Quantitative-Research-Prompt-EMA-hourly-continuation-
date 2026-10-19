# EMA Hourly Continuation — TIA/USDT P12_26

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1404 |
| net_profit_factor | 0.4905 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -9.6914 |
| sortino_ratio | -5.1085 |
| max_drawdown | 0.9984 |
| cagr | -0.9225 |
| net_avg_win | 15.4995 |
| net_avg_loss | -24.9917 |
| avg_hold_time_bars | 2.7764 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
