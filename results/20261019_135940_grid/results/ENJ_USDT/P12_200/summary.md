# EMA Hourly Continuation — ENJ/USDT P12_200

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.6970 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 0.9443 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.0103 |
| sortino_ratio | -0.5153 |
| max_drawdown | 0.5060 |
| cagr | -0.2190 |
| net_avg_win | 66.0792 |
| net_avg_loss | -89.2558 |
| avg_hold_time_bars | 51.1114 |
| exposure | 0.7713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
