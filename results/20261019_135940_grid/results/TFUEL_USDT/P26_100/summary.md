# EMA Hourly Continuation — TFUEL/USDT P26_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 805 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4149 |
| sharpe_ratio | -7.3880 |
| sortino_ratio | -2.9376 |
| max_drawdown | 0.9742 |
| cagr | -0.7622 |
| net_avg_win | 30.1191 |
| net_avg_loss | -41.1154 |
| avg_hold_time_bars | 9.0286 |
| exposure | 0.3289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
