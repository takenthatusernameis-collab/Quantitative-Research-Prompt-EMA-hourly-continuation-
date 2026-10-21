# EMA Hourly Continuation — SEI/USDT P55_89

**Symbol:** SEI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9016 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -1.8344 |
| sortino_ratio | -0.4310 |
| max_drawdown | 0.3908 |
| cagr | -0.1791 |
| net_avg_win | 64.2154 |
| net_avg_loss | -87.5418 |
| avg_hold_time_bars | 7.6741 |
| exposure | 0.0942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
