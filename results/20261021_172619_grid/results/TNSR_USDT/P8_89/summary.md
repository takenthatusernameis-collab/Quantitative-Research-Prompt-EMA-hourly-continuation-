# EMA Hourly Continuation — TNSR/USDT P8_89

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.8549 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0251 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.2905 |
| sortino_ratio | -0.4482 |
| max_drawdown | 0.4994 |
| cagr | -0.1891 |
| net_avg_win | 81.2025 |
| net_avg_loss | -96.6037 |
| avg_hold_time_bars | 22.1709 |
| exposure | 0.5930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
