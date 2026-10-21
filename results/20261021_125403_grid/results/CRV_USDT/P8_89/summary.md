# EMA Hourly Continuation — CRV/USDT P8_89

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9719 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.4510 |
| sortino_ratio | -0.4402 |
| max_drawdown | 0.4361 |
| cagr | -0.1847 |
| net_avg_win | 77.2981 |
| net_avg_loss | -92.4542 |
| avg_hold_time_bars | 31.8714 |
| exposure | 0.6534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
