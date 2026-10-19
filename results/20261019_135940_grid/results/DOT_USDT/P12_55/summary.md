# EMA Hourly Continuation — DOT/USDT P12_55

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.5437 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -5.6993 |
| sortino_ratio | -2.3877 |
| max_drawdown | 0.9489 |
| cagr | -0.6901 |
| net_avg_win | 26.8077 |
| net_avg_loss | -44.0728 |
| avg_hold_time_bars | 10.6805 |
| exposure | 0.4330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
