# EMA Hourly Continuation — DOT/USDT P8_26

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.7514 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0608 |
| gross_win_rate | 0.5151 |
| sharpe_ratio | -2.1999 |
| sortino_ratio | -0.7952 |
| max_drawdown | 0.6359 |
| cagr | -0.3039 |
| net_avg_win | 55.7088 |
| net_avg_loss | -78.7635 |
| avg_hold_time_bars | 6.6757 |
| exposure | 0.1909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
