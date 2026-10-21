# EMA Hourly Continuation — AXL/USDT P20_21

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.4739 |
| net_win_rate | 0.3973 |
| gross_profit_factor | 0.6709 |
| gross_win_rate | 0.3973 |
| sharpe_ratio | -3.5928 |
| sortino_ratio | -0.7630 |
| max_drawdown | 0.6162 |
| cagr | -0.3003 |
| net_avg_win | 60.0882 |
| net_avg_loss | -83.5994 |
| avg_hold_time_bars | 4.9732 |
| exposure | 0.0504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
