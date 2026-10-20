# EMA Hourly Continuation — ARKM/USDT P12_200

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.1561 |
| sortino_ratio | -0.6043 |
| max_drawdown | 0.5313 |
| cagr | -0.2494 |
| net_avg_win | 63.9755 |
| net_avg_loss | -83.1226 |
| avg_hold_time_bars | 40.8719 |
| exposure | 0.7394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
