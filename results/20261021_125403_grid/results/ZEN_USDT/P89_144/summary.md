# EMA Hourly Continuation — ZEN/USDT P89_144

**Symbol:** ZEN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6111 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8152 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -2.8153 |
| sortino_ratio | -0.7014 |
| max_drawdown | 0.5671 |
| cagr | -0.2771 |
| net_avg_win | 64.3783 |
| net_avg_loss | -83.7915 |
| avg_hold_time_bars | 7.7818 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
