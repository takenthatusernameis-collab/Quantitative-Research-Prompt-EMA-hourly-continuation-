# EMA Hourly Continuation — VET/USDT P21_89

**Symbol:** VET/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.6684 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 1.0833 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -3.8285 |
| sortino_ratio | -1.4646 |
| max_drawdown | 0.8428 |
| cagr | -0.5051 |
| net_avg_win | 45.2777 |
| net_avg_loss | -67.9290 |
| avg_hold_time_bars | 10.8033 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
