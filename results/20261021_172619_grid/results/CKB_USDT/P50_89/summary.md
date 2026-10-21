# EMA Hourly Continuation — CKB/USDT P50_89

**Symbol:** CKB/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7261 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9880 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -2.2825 |
| sortino_ratio | -0.6216 |
| max_drawdown | 0.5562 |
| cagr | -0.2484 |
| net_avg_win | 77.5189 |
| net_avg_loss | -99.9166 |
| avg_hold_time_bars | 7.8260 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
