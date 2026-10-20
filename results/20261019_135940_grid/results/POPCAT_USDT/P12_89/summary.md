# EMA Hourly Continuation — POPCAT/USDT P12_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8279 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -4.3964 |
| sortino_ratio | -1.5824 |
| max_drawdown | 0.8138 |
| cagr | -0.5396 |
| net_avg_win | 47.9998 |
| net_avg_loss | -64.0025 |
| avg_hold_time_bars | 18.8278 |
| exposure | 0.5719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
