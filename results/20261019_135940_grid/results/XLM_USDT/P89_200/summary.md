# EMA Hourly Continuation — XLM/USDT P89_200

**Symbol:** XLM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.4269 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7867 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -4.6801 |
| sortino_ratio | -1.3160 |
| max_drawdown | 0.8022 |
| cagr | -0.4735 |
| net_avg_win | 34.4544 |
| net_avg_loss | -62.0622 |
| avg_hold_time_bars | 10.0955 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
