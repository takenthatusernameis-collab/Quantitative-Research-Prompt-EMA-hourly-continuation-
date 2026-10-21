# EMA Hourly Continuation — NMR/USDT P12_200

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8492 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0091 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -0.8483 |
| sortino_ratio | -0.2278 |
| max_drawdown | 0.3361 |
| cagr | -0.1022 |
| net_avg_win | 74.6631 |
| net_avg_loss | -90.9675 |
| avg_hold_time_bars | 43.9233 |
| exposure | 0.7028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
