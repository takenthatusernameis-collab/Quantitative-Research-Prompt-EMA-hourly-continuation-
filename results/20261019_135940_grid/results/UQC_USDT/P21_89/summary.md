# EMA Hourly Continuation — UQC/USDT P21_89

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.2657 |
| net_win_rate | 0.2776 |
| gross_profit_factor | 0.4877 |
| gross_win_rate | 0.3116 |
| sharpe_ratio | -8.3012 |
| sortino_ratio | -2.2078 |
| max_drawdown | 0.9584 |
| cagr | -0.7165 |
| net_avg_win | 35.3787 |
| net_avg_loss | -51.1795 |
| avg_hold_time_bars | 32.1473 |
| exposure | 0.5136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
