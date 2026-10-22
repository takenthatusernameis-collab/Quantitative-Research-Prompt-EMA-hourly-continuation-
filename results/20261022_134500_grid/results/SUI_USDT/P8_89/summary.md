# EMA Hourly Continuation — SUI/USDT P8_89

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.6087 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -5.1052 |
| sortino_ratio | -1.9373 |
| max_drawdown | 0.9171 |
| cagr | -0.6227 |
| net_avg_win | 41.1960 |
| net_avg_loss | -57.7909 |
| avg_hold_time_bars | 17.8131 |
| exposure | 0.6065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
