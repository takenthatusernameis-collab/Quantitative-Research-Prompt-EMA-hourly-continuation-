# EMA Hourly Continuation — AVAX/USDT P89_100

**Symbol:** AVAX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.2258 |
| net_win_rate | 0.3804 |
| gross_profit_factor | 0.6866 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -9.7676 |
| sortino_ratio | -3.3618 |
| max_drawdown | 0.9905 |
| cagr | -0.8427 |
| net_avg_win | 13.7523 |
| net_avg_loss | -37.4030 |
| avg_hold_time_bars | 1.8768 |
| exposure | 0.0471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
