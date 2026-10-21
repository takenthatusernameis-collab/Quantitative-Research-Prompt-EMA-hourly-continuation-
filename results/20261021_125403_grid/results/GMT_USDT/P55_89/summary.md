# EMA Hourly Continuation — GMT/USDT P55_89

**Symbol:** GMT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -2.6210 |
| sortino_ratio | -0.6485 |
| max_drawdown | 0.5457 |
| cagr | -0.2574 |
| net_avg_win | 65.3216 |
| net_avg_loss | -86.6651 |
| avg_hold_time_bars | 6.3987 |
| exposure | 0.0875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
