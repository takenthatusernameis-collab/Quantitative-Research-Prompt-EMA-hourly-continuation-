# EMA Hourly Continuation — BIGTIME/USDT P21_200

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0214 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.1361 |
| sortino_ratio | -0.2963 |
| max_drawdown | 0.3645 |
| cagr | -0.1311 |
| net_avg_win | 78.5651 |
| net_avg_loss | -97.1611 |
| avg_hold_time_bars | 42.8618 |
| exposure | 0.6595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
