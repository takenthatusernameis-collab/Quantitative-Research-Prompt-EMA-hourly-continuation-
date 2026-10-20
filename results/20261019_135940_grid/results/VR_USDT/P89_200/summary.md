# EMA Hourly Continuation — VR/USDT P89_200

**Symbol:** VR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.3682 |
| net_win_rate | 0.2835 |
| gross_profit_factor | 0.5647 |
| gross_win_rate | 0.2913 |
| sharpe_ratio | -9.9043 |
| sortino_ratio | -3.1611 |
| max_drawdown | 0.9892 |
| cagr | -0.8333 |
| net_avg_win | 40.0287 |
| net_avg_loss | -43.0025 |
| avg_hold_time_bars | 8.7362 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
