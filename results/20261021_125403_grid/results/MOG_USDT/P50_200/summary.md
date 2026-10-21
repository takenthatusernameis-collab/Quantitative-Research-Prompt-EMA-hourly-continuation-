# EMA Hourly Continuation — MOG/USDT P50_200

**Symbol:** MOG/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.8495 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9913 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -0.8571 |
| sortino_ratio | -0.2117 |
| max_drawdown | 0.2735 |
| cagr | -0.0945 |
| net_avg_win | 83.9687 |
| net_avg_loss | -99.5685 |
| avg_hold_time_bars | 26.6520 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
