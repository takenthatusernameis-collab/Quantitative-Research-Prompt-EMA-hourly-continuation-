# EMA Hourly Continuation — XLM/USDT P12_20

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.5598 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8718 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.5932 |
| sortino_ratio | -0.5760 |
| max_drawdown | 0.4930 |
| cagr | -0.2316 |
| net_avg_win | 54.4849 |
| net_avg_loss | -87.2803 |
| avg_hold_time_bars | 5.8285 |
| exposure | 0.0633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
