# EMA Hourly Continuation — CVX/USDT P21_200

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7676 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9941 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -1.3918 |
| sortino_ratio | -0.3359 |
| max_drawdown | 0.3622 |
| cagr | -0.1482 |
| net_avg_win | 75.5434 |
| net_avg_loss | -96.4181 |
| avg_hold_time_bars | 51.8225 |
| exposure | 0.6902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
