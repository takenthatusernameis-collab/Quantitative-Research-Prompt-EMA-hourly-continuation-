# EMA Hourly Continuation — AMP/USDT P144_200

**Symbol:** AMP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.4587 |
| net_win_rate | 0.3909 |
| gross_profit_factor | 0.6580 |
| gross_win_rate | 0.3909 |
| sharpe_ratio | -3.8006 |
| sortino_ratio | -0.8424 |
| max_drawdown | 0.6313 |
| cagr | -0.3236 |
| net_avg_win | 55.7835 |
| net_avg_loss | -78.0623 |
| avg_hold_time_bars | 7.9259 |
| exposure | 0.0875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
