# EMA Hourly Continuation — BAT/USDT P50_89

**Symbol:** BAT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.6288 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9272 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -2.7644 |
| sortino_ratio | -0.7946 |
| max_drawdown | 0.6196 |
| cagr | -0.3040 |
| net_avg_win | 51.9005 |
| net_avg_loss | -77.7559 |
| avg_hold_time_bars | 6.5746 |
| exposure | 0.1201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
