# EMA Hourly Continuation — FLOKI/USDT P20_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8171 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9439 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -1.0411 |
| sortino_ratio | -0.2437 |
| max_drawdown | 0.2843 |
| cagr | -0.1075 |
| net_avg_win | 84.7090 |
| net_avg_loss | -97.7065 |
| avg_hold_time_bars | 53.9815 |
| exposure | 0.6625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
