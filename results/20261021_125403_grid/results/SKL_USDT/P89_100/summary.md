# EMA Hourly Continuation — SKL/USDT P89_100

**Symbol:** SKL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 117 |
| net_profit_factor | 0.6264 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -1.4713 |
| sortino_ratio | -0.2282 |
| max_drawdown | 0.2404 |
| cagr | -0.0990 |
| net_avg_win | 68.9844 |
| net_avg_loss | -101.1008 |
| avg_hold_time_bars | 4.8205 |
| exposure | 0.0256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
