# EMA Hourly Continuation — ZEC/USDT P8_89

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.9113 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0645 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -0.5401 |
| sortino_ratio | -0.1684 |
| max_drawdown | 0.3157 |
| cagr | -0.0801 |
| net_avg_win | 79.6458 |
| net_avg_loss | -94.3561 |
| avg_hold_time_bars | 29.5766 |
| exposure | 0.6319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
