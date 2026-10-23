# EMA Hourly Continuation — ZRX/USDT P12_34

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1252 |
| net_profit_factor | 0.4119 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8114 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -8.8352 |
| sortino_ratio | -4.4146 |
| max_drawdown | 0.9955 |
| cagr | -0.8839 |
| net_avg_win | 12.5652 |
| net_avg_loss | -24.2881 |
| avg_hold_time_bars | 4.6861 |
| exposure | 0.2667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
