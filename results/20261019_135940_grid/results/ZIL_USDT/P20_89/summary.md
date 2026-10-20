# EMA Hourly Continuation — ZIL/USDT P20_89

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9946 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -5.2205 |
| sortino_ratio | -2.0002 |
| max_drawdown | 0.9221 |
| cagr | -0.6229 |
| net_avg_win | 38.2031 |
| net_avg_loss | -55.9314 |
| avg_hold_time_bars | 10.6331 |
| exposure | 0.3596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
