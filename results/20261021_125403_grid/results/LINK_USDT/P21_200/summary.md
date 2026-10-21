# EMA Hourly Continuation — LINK/USDT P21_200

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.9058 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1201 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.5021 |
| sortino_ratio | -0.1267 |
| max_drawdown | 0.2555 |
| cagr | -0.0594 |
| net_avg_win | 84.5896 |
| net_avg_loss | -105.0605 |
| avg_hold_time_bars | 40.2288 |
| exposure | 0.5595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
