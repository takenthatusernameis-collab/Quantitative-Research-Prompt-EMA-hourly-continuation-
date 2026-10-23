# EMA Hourly Continuation — IOTX/USDT P21_89

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.5741 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -5.0988 |
| sortino_ratio | -1.9676 |
| max_drawdown | 0.9075 |
| cagr | -0.6079 |
| net_avg_win | 35.6566 |
| net_avg_loss | -52.1921 |
| avg_hold_time_bars | 10.3992 |
| exposure | 0.3540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
