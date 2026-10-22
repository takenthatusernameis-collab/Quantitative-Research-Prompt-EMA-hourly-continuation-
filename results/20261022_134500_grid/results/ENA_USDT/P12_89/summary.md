# EMA Hourly Continuation — ENA/USDT P12_89

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.8070 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0534 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -1.9126 |
| sortino_ratio | -0.7320 |
| max_drawdown | 0.6226 |
| cagr | -0.2907 |
| net_avg_win | 65.4893 |
| net_avg_loss | -84.8300 |
| avg_hold_time_bars | 15.9571 |
| exposure | 0.5237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
