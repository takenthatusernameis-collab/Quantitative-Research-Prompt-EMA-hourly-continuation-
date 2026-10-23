# EMA Hourly Continuation — ZRX/USDT P50_200

**Symbol:** ZRX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.7028 |
| sortino_ratio | -0.8030 |
| max_drawdown | 0.6238 |
| cagr | -0.3155 |
| net_avg_win | 53.4574 |
| net_avg_loss | -77.7874 |
| avg_hold_time_bars | 18.3614 |
| exposure | 0.3672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
