# EMA Hourly Continuation — DOT/USDT P8_55

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0229 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.7600 |
| sortino_ratio | -0.6235 |
| max_drawdown | 0.5513 |
| cagr | -0.2498 |
| net_avg_win | 63.1653 |
| net_avg_loss | -82.1960 |
| avg_hold_time_bars | 18.0673 |
| exposure | 0.5001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
