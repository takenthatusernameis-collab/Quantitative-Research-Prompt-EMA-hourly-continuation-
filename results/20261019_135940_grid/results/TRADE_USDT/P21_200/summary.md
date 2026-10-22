# EMA Hourly Continuation — TRADE/USDT P21_200

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7676 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -1.4891 |
| sortino_ratio | -0.3860 |
| max_drawdown | 0.3875 |
| cagr | -0.1657 |
| net_avg_win | 74.5180 |
| net_avg_loss | -91.4394 |
| avg_hold_time_bars | 38.2754 |
| exposure | 0.5811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
