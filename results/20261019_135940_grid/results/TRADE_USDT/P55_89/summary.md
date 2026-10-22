# EMA Hourly Continuation — TRADE/USDT P55_89

**Symbol:** TRADE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.3813 |
| net_win_rate | 0.3750 |
| gross_profit_factor | 0.6447 |
| gross_win_rate | 0.3808 |
| sharpe_ratio | -6.9688 |
| sortino_ratio | -2.2408 |
| max_drawdown | 0.9436 |
| cagr | -0.6783 |
| net_avg_win | 29.7780 |
| net_avg_loss | -46.8533 |
| avg_hold_time_bars | 5.5635 |
| exposure | 0.1315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
