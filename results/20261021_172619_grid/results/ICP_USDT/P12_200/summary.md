# EMA Hourly Continuation — ICP/USDT P12_200

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.8544 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -0.7586 |
| sortino_ratio | -0.1765 |
| max_drawdown | 0.2221 |
| cagr | -0.0800 |
| net_avg_win | 83.3438 |
| net_avg_loss | -98.2855 |
| avg_hold_time_bars | 61.8151 |
| exposure | 0.7446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
