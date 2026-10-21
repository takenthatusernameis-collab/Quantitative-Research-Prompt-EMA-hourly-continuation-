# EMA Hourly Continuation — ZBCN/USDT P21_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.9770 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1164 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -0.0927 |
| sortino_ratio | -0.0267 |
| max_drawdown | 0.2686 |
| cagr | -0.0194 |
| net_avg_win | 96.2835 |
| net_avg_loss | -111.4060 |
| avg_hold_time_bars | 28.6888 |
| exposure | 0.5203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
