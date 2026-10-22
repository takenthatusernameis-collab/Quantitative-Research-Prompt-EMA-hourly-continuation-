# EMA Hourly Continuation — ETH/USDT P55_200

**Symbol:** ETH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.5096 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -3.5696 |
| sortino_ratio | -0.9509 |
| max_drawdown | 0.6943 |
| cagr | -0.3657 |
| net_avg_win | 41.4002 |
| net_avg_loss | -75.0874 |
| avg_hold_time_bars | 23.1124 |
| exposure | 0.3740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
