# EMA Hourly Continuation — AURORA/USDT P8_89

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7649 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.1915 |
| sortino_ratio | -0.7023 |
| max_drawdown | 0.6123 |
| cagr | -0.2775 |
| net_avg_win | 74.4042 |
| net_avg_loss | -90.5891 |
| avg_hold_time_bars | 25.8024 |
| exposure | 0.5935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
