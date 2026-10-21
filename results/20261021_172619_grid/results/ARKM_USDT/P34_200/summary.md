# EMA Hourly Continuation — ARKM/USDT P34_200

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7965 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9265 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -1.1871 |
| sortino_ratio | -0.3062 |
| max_drawdown | 0.3306 |
| cagr | -0.1328 |
| net_avg_win | 74.0520 |
| net_avg_loss | -87.9871 |
| avg_hold_time_bars | 32.3976 |
| exposure | 0.4815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
