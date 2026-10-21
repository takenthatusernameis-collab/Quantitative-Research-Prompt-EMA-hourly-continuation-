# EMA Hourly Continuation — BTC/USDT P12_20

**Symbol:** BTC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.4365 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -3.6241 |
| sortino_ratio | -0.8212 |
| max_drawdown | 0.6600 |
| cagr | -0.3144 |
| net_avg_win | 39.2952 |
| net_avg_loss | -80.1519 |
| avg_hold_time_bars | 6.3116 |
| exposure | 0.0697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
