# EMA Hourly Continuation — AXS/USDT P21_55

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5147 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -1.6221 |
| sortino_ratio | -0.5081 |
| max_drawdown | 0.4669 |
| cagr | -0.2079 |
| net_avg_win | 68.8775 |
| net_avg_loss | -92.2943 |
| avg_hold_time_bars | 8.7542 |
| exposure | 0.1886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
