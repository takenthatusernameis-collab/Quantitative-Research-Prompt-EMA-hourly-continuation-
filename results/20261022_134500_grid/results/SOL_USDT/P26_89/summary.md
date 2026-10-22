# EMA Hourly Continuation — SOL/USDT P26_89

**Symbol:** SOL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -5.3883 |
| sortino_ratio | -2.0041 |
| max_drawdown | 0.9223 |
| cagr | -0.6278 |
| net_avg_win | 36.4709 |
| net_avg_loss | -57.4941 |
| avg_hold_time_bars | 8.3889 |
| exposure | 0.2677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
