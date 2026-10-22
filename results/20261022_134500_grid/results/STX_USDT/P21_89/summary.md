# EMA Hourly Continuation — STX/USDT P21_89

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6071 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -4.4866 |
| sortino_ratio | -1.6604 |
| max_drawdown | 0.8723 |
| cagr | -0.5481 |
| net_avg_win | 41.5147 |
| net_avg_loss | -59.0330 |
| avg_hold_time_bars | 11.8460 |
| exposure | 0.3726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
