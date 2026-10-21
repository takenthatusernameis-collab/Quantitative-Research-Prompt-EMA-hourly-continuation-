# EMA Hourly Continuation — TWT/USDT P12_200

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.8488 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0586 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -0.8168 |
| sortino_ratio | -0.2052 |
| max_drawdown | 0.3045 |
| cagr | -0.0922 |
| net_avg_win | 76.6474 |
| net_avg_loss | -96.3976 |
| avg_hold_time_bars | 53.2614 |
| exposure | 0.7408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
