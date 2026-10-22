# EMA Hourly Continuation — ADA/USDT P8_89

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.5892 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -4.4851 |
| sortino_ratio | -1.6991 |
| max_drawdown | 0.8768 |
| cagr | -0.5581 |
| net_avg_win | 36.6562 |
| net_avg_loss | -55.2433 |
| avg_hold_time_bars | 18.5848 |
| exposure | 0.6125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
