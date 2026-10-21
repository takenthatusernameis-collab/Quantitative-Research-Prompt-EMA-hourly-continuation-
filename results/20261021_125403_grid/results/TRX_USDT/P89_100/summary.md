# EMA Hourly Continuation — TRX/USDT P89_100

**Symbol:** TRX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.2029 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.6571 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -3.6231 |
| sortino_ratio | -0.4893 |
| max_drawdown | 0.4428 |
| cagr | -0.2054 |
| net_avg_win | 37.2151 |
| net_avg_loss | -112.3163 |
| avg_hold_time_bars | 6.8228 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
