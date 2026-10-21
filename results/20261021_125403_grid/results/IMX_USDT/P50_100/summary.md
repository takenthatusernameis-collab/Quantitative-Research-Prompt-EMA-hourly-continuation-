# EMA Hourly Continuation — IMX/USDT P50_100

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8416 |
| net_win_rate | 0.5230 |
| gross_profit_factor | 1.0836 |
| gross_win_rate | 0.5230 |
| sharpe_ratio | -0.9943 |
| sortino_ratio | -0.2832 |
| max_drawdown | 0.3062 |
| cagr | -0.1235 |
| net_avg_win | 73.2975 |
| net_avg_loss | -95.4797 |
| avg_hold_time_bars | 7.5153 |
| exposure | 0.1333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
