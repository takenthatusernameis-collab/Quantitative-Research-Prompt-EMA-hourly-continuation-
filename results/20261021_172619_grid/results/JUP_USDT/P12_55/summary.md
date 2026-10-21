# EMA Hourly Continuation — JUP/USDT P12_55

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.8279 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.6697 |
| sortino_ratio | -0.6128 |
| max_drawdown | 0.5611 |
| cagr | -0.2472 |
| net_avg_win | 74.5415 |
| net_avg_loss | -90.5891 |
| avg_hold_time_bars | 11.0503 |
| exposure | 0.3295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
