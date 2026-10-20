# EMA Hourly Continuation — KNC/USDT P8_89

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6106 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -4.2138 |
| sortino_ratio | -1.4356 |
| max_drawdown | 0.8238 |
| cagr | -0.4961 |
| net_avg_win | 47.5124 |
| net_avg_loss | -66.3117 |
| avg_hold_time_bars | 25.6740 |
| exposure | 0.6874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
